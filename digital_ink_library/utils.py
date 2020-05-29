from scipy.spatial import ConvexHull
import math
import numpy as np


def bounding_box(strokes):
    x_max = []
    x_min = []
    y_max = []
    y_min = []

    for x, y, t, p in strokes:
        x_max.append(max(x))
        x_min.append(min(x))
        y_max.append(max(y))
        y_min.append(min(y))

    return min(x_min), min(y_min), max(x_max), max(y_max)


def convex_hull(strokes):
    x_all = []
    y_all = []

    for x, y, t, p in strokes:
        for x_i in x:
            x_all.append(x_i)
        for y_i in y:
            y_all.append(y_i)

    np_x = np.array(x_all).reshape((-1, 1))
    np_y = np.array(y_all).reshape((-1, 1))
    pts = np.hstack((np_x, np_y))
    return ConvexHull(pts)


def convex_hull_major_minor(strokes):
    pts = []

    for x, y, t, p in strokes:
        for i in range(0, len(x)):
            x_i = x[i]
            y_i = y[i]
            pts.append((x_i, y_i))

    bounding_box = minimum_bounding_box(pts)
    minor = min(bounding_box.length_parallel, bounding_box.length_orthogonal)
    major = max(bounding_box.length_parallel, bounding_box.length_orthogonal)

    return major, minor


def centroid(strokes):
    x_all = []
    y_all = []

    for x, y, t, p in strokes:
        for x_i in x:
            x_all.append(x_i)
        for y_i in y:
            y_all.append(y_i)

    np_x = np.asarray(x_all)
    np_y = np.asarray(y_all)

    length = float(len(x_all))
    sum_x = np.sum(np_x)
    sum_y = np.sum(np_y)
    return sum_x / length, sum_y / length


def mean_centroid_distance(strokes):
    c = centroid(strokes)
    n = 0
    s = 0.0
    for x, y, t, p in strokes:
        for i in range(0, len(x)):
            d = math.sqrt((c[0] - x[i]) ** 2 + (c[1] - y[i]) ** 2)
            s += d
            n += 1

    return s / n


def convert_myscript_ink(arr):
    strokes = []
    for stroke in arr:
        x = []
        y = []
        for i in range(0, len(stroke) - 1, 2):
            x.append(stroke[i])
            y.append(stroke[i + 1])
        strokes.append((x, y, [], []))

    return strokes


def print_probabilites(self, probabilities):
    for i in range(0, len(probabilities)):
        print(self.labels[i], probabilities[i])
