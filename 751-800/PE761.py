# Project Euler 761

####### User Modules #######
from plotter import plotter
from timer import timer
from debugger import debug, debug_table
from matplotlib.animation import FuncAnimation


####### PyPi Packages #######
#from numba import jit
from math import pi, sin, cos
import numpy as np


@plotter(plot=True)
@timer
#@jit(nopython=True, fastmath=True, nogil=True)  # , parallel=True)
def shape(sides, shape_acc, point_slow, point_num, run_speed, ax):
    # Get all points of polygon
    shape, verticies = parameterise_polygon(sides, acc=shape_acc)
    run = np.array([-1, 0])
    swim = np.array([0, 0])
    for ind, i in enumerate(shape):
        ax.scatter(i[:, 0], i[:, 1], label=ind)
    ax.scatter(np.array([0]), np.array([0]), label="centre")
    #find_best(shape, verticies, run, swim, sides, acc, 5, ax)
    for i in range(point_num):
        run, swim = find_best(shape, verticies, run,
                              swim, sides, acc2=point_slow, speed=run_speed, ax=ax)


def find_best(shape, verticies, run, swim, sides, acc2, speed, ax):
    seg_length = distance(verticies[1], verticies[0])

    # Find distance to swimmer for each point:
    distances_swim = distance(shape, swim, 2)

    # Find (signed) distance to runner (via perimeter) for each point:
    v_dist = distance(verticies, run, 1)
    if v_dist[-1] < seg_length and v_dist[0] < seg_length:
        seg_run = 0
    else:
        seg_run = np.min(np.where(v_dist < seg_length))+1
    run_to_v = distance(verticies[seg_run], run)
    distances = np.full(
        shape.shape[:2], sides*seg_length+0.1)
    for seg_point, edge in enumerate(shape):
        seg_num = (seg_point - seg_run - 1) % sides
        for j, point in enumerate(edge):
            if seg_run == seg_point:
                if any(np.round(abs(verticies[seg_run] - run), 6) > np.round(abs(verticies[seg_run] - point), 6)):
                    dist = distance(point, run)
                    #print("PING", point, dist)
                    distances[seg_point, j] = dist
                    continue
                else:
                    seg_num = 3
            v_to_point = distance(point, verticies[seg_point-1])
            dist1 = seg_length * seg_num + run_to_v + v_to_point
            dist2 = dist1 - 8
            if dist1 <= abs(dist2):
                dist = dist1
            else:
                dist = dist2
            distances[seg_point, j] = dist
    distances_run = np.array(distances)

    # Combine to form rankings and find the best point
    rankings = np.dstack([shape, distances_run / distances_swim])
    max_ind = np.argmax(abs(rankings[:, :, 2].flatten()))
    ind = np.unravel_index(max_ind, rankings[:, :, 2].shape)
    best = rankings[ind]
    #print(best)

    # Plot points
    ax.scatter(swim[0], swim[1], label="Swimmer", s=50, c="#bb00bb")
    ax.scatter(run[0], run[1], label="Runner", s=50, c="#dd0000")
    ax.scatter(best[0], best[1], label="Best Point", s=50, c="#00dd00")
    swim_dir = (best[:2]-swim) / distance(best[:2], swim)
    swim = swim + swim_dir / acc2
    if best[2] > 0:
        if distance(verticies[seg_run], run) < seg_length:
            seg_run += 1
        run_dir = (verticies[seg_run]-run) / \
            distance(verticies[seg_run], run)
    else:
        if distance(verticies[seg_run-1], run) < seg_length:
            seg_run -= 1
        run_dir = (verticies[seg_run-1]-run) / \
            distance(verticies[seg_run-1], run)
    run = run + speed * run_dir / acc2
    return run, swim


def distance(a, b, axis=0):
    return np.sum((a - b) ** 2, axis=axis) ** 0.5


def parameterise_polygon(n: int, acc: int) -> np.array:
    # Find vertex vectors
    theta = 2 * pi / n
    scale = 1 / sin(pi / 2 - pi / n)
    if n % 2 == 0:
        verticies = scale * np.array(
            [[round(cos(i * theta + pi / n), 12), round(sin(i * theta + pi / n), 12)] for i in range(n)])
    else:
        verticies = scale * np.array(
            [[round(cos(i * theta), 12), round(sin(i * theta), 12)] for i in range(n)])

    # Make parametric equation based of line segments between verticies
    vector_pairs = [[verticies[i-1], verticies[i]]
                    for i in range(len(verticies))]
    equations = [parameterise_line(vertex1, vertex2)
                 for vertex1, vertex2 in vector_pairs]
    points = np.array([np.array([np.array(func(t/acc))
                      for t in range(acc)]) for i, func in enumerate(equations)])
    return points, verticies


def parameterise_line(vertex1, vertex2):
    return lambda t: vertex2 - t * (vertex2 - vertex1)


shape(5, shape_acc=50, point_slow=5, point_num=5, run_speed=2)
#debug_table()
