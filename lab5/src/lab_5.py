from collections import deque


def read_input_file(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    start = tuple(map(int, lines[0].split(',')))
    end = tuple(map(int, lines[1].split(',')))
    rows, cols = map(int, lines[2].split(','))

    matrix = [list(map(int, line.strip('[]').split())) for line in lines[3:]]

    return start, end, matrix


def dfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def search(x, y):
        if not (0 <= x < rows and 0 <= y < cols) or matrix[x][y] == 0 or visited[x][y]:
            return False

        visited[x][y] = True

        if (x, y) == end:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if search(nx, ny):
                parent[nx][ny] = (x, y)
                return True

        return False

    if search(start[0], start[1]):
        return reconstruct_path(parent, start, end)

    return []


def reconstruct_path(parent, start, end):
    path = []
    x, y = end
    while (x, y) != start:
        path.append((x, y))
        x, y = parent[x][y]
    path.append(start)
    path.reverse()
    return path


def write_output_file(filename, result, path):
    with open(filename, 'w') as f:
        if result == -1:
            f.write("Path not found\n")
        else:
            f.write(f"Shortest path length: {len(path) - 1}\n")
            f.write("Path coordinates:\n")
            for p in path:
                f.write(f"({p[0]}, {p[1]})")


if __name__ == "__main__":
    start, end, matrix = read_input_file("../test/input.txt")
    path = dfs(matrix, start, end)

    if path:
        write_output_file("output.txt", len(path) - 1, path)
    else:
        write_output_file("output.txt", -1, [])
