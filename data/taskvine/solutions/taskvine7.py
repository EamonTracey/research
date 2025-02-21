# TODO: fix

import random

import ndcctools.taskvine as vine
import numpy

def invert_matrix(matrix):
    import numpy
    matrix = numpy.array(matrix)
    return numpy.linalg.inv(matrix)

def transpose_matrix(matrix):
    import numpy
    matrix = numpy.array(matrix)
    return matrix.T

manager = vine.Manager()
poncho_file = manager.declare_file("library_env.tar.gz", cache="workflow")
poncho_env = manager.declare_poncho(poncho_file, cache="workflow")
matrix_library = manager.create_library_from_functions("matrix_library", invert_matrix, transpose_matrix, poncho_env=poncho_env)
manager.install_library(matrix_library)

m = int(input("m: "))
n = int(input("n: "))
i = int(input("i: "))

for _ in range(i):
    matrix = [[random.random() for _ in range(n)] for _ in range(m)]
    print(matrix)
    task = vine.FunctionCall("matrix_library", "invert_matrix", matrix)
    manager.submit(task)
    task = vine.FunctionCall("matrix_library", "transpose_matrix", matrix)
    manager.submit(task)

while not manager.empty():
    task = manager.wait()
    print(task.result())
