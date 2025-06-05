from collections import defaultdict, deque

def read_dependencies(filename: str):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_nodes = set()

    with open(filename, "r") as f:
        for line in f:
            if not line.strip():
                continue
            a, b = line.strip().split()
            graph[a].append(b)         # a → b
            in_degree[b] += 1
            all_nodes.update([a, b])

    for node in all_nodes:
        in_degree.setdefault(node, 0)

    return graph, in_degree

def topological_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(in_degree):
        raise ValueError("Цикл у графі або помилка в даних")

    return result

def main():
    graph, in_degree = read_dependencies("../test/govern.in")
    order = topological_sort(graph, in_degree)
    print("Order:", order)
    with open("../test/govern.out", "w") as f:
        for item in order:
            f.write(item + "\n")

if __name__ == "__main__":
    main()


