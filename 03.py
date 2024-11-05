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
def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes()}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph.nodes()}
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        
        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break
        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight
            
            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    # Відновлення шляхів
    paths = {vertex: [] for vertex in graph.nodes()}
    for vertex in graph.nodes():
        if distances[vertex] == float('infinity'):
            continue
        current = vertex
        while current is not None:
            paths[vertex].insert(0, current)
            current = previous_nodes[current]

    return distances, paths

# Знаходження найкоротших шляхів між усіма вершинами
shortest_paths = {}
for start_node in metro_graph.nodes:
    length, path = dijkstra(metro_graph, start_node)
    shortest_paths[start_node] = (length, path)

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
