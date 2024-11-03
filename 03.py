import networkx as nx
import matplotlib.pyplot as plt


metro_graph = nx.Graph()
metro_graph.add_edge('Академмістечко', 'Житомирська', weight=2)
metro_graph.add_edge('Житомирська', 'Святошин', weight=1)
metro_graph.add_edge('Святошин', 'Нивки', weight=2)
metro_graph.add_edge('Нивки', 'Берестейська', weight=1)
metro_graph.add_edge('Берестейська', 'Шулявська', weight=2)
metro_graph.add_edge('Шулявська', 'Політехнічний інститут', weight=1)
metro_graph.add_edge('Політехнічний інститут', 'Вокзальна', weight=3)
metro_graph.add_edge('Вокзальна', 'Університет', weight=1)
metro_graph.add_edge('Університет', 'Театральна', weight=1)
metro_graph.add_edge('Театральна', 'Хрещатик', weight=1)
metro_graph.add_edge('Хрещатик', 'Арсенальна', weight=2)
metro_graph.add_edge('Арсенальна', 'Дніпро', weight=3)
metro_graph.add_edge('Дніпро', 'Гідропарк', weight=1)
metro_graph.add_edge('Гідропарк', 'Лівобережна', weight=2)
metro_graph.add_edge('Лівобережна', 'Дарниця', weight=3)
metro_graph.add_edge('Дарниця', 'Чернігівська', weight=1)
metro_graph.add_edge('Чернігівська', 'Лісова', weight=1)

# Функція для виконання алгоритму Дейкстри
def dijkstra_all_paths(graph):
    all_paths = {}
    for node in graph.nodes():
        length, path = nx.single_source_dijkstra(graph, node)
        all_paths[node] = (length, path)
    return all_paths

# Знаходження найкоротших шляхів між усіма вершинами
shortest_paths = dijkstra_all_paths(metro_graph)

# Результат
for start_node, (length, path) in shortest_paths.items():
    for end_node, dist in length.items():
        print(f"Найкоротший шлях з {start_node} до {end_node}: {path[end_node]} з вагою {dist} хвилин")

# Візуалізація
pos = nx.spring_layout(metro_graph)
nx.draw(metro_graph, pos, with_labels=True, node_size=100, node_color='lightblue', font_size=6)
edge_labels = nx.get_edge_attributes(metro_graph, 'weight')
nx.draw_networkx_edge_labels(metro_graph, pos, edge_labels=edge_labels)
plt.title("Граф метро Києва з вагами")
plt.show()
