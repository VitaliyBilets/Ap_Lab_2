import csv
import math

def read_adjacency_matrix(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        matrix = []
        for row in reader:
            matrix.append([float(cell) for cell in row])
    return matrix

def prim_mst(matrix):
    n = len(matrix)
    selected = [False] * n
    min_edge = [math.inf] * n
    min_edge[0] = 0
    total_weight = 0

    for _ in range(n):

        u = -1
        for v in range(n):
            if not selected[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u = v

        if min_edge[u] == math.inf:
            raise ValueError

        selected[u] = True
        total_weight += min_edge[u]


        for v in range(n):
            if matrix[u][v] > 0 and not selected[v] and matrix[u][v] < min_edge[v]:
                min_edge[v] = matrix[u][v]

    return total_weight



matrix = read_adjacency_matrix('islands.csv')
total_cable_length = prim_mst(matrix)
print(f"Мінімальна довжина кабелю: {total_cable_length}")
