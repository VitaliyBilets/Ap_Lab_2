import csv
import networkx as nx
import matplotlib.pyplot as plt

def read_adjacency_matrix(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        matrix = []
        for row in reader:
            matrix.append([float(cell) for cell in row])
    return matrix

def build_graph(matrix):
    G = nx.Graph()
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            weight = matrix[i][j]
            if weight > 0:
                G.add_edge(i, j, weight=weight)
    return G

def draw_graph(matrix):
    G = build_graph(matrix)
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Візуалізація графа ")
    plt.show()

if __name__ == '__main__':
    matrix = read_adjacency_matrix('islands.csv')
    draw_graph(matrix)
