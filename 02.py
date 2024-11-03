import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф метро
metro_graph = nx.Graph()

# Додаємо станції як вершини та лінії як ребра
red_line = [
    "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська",
    "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет",
    "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк",
    "Лівобережна", "Дарниця", "Чернігівська", "Лісова"
]
red_edges = [(red_line[i], red_line[i + 1]) for i in range(len(red_line) - 1)]
metro_graph.add_edges_from(red_edges)

blue_line = [
    "Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка",
    "Контрактова площа", "Поштова площа", "Майдан Незалежності",
    "Площа Льва Толстого", "Олімпійська", "Палац Україна", "Либідська",
    "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр",
    "Іподром", "Теремки"
]
blue_edges = [(blue_line[i], blue_line[i + 1]) for i in range(len(blue_line) - 1)]
metro_graph.add_edges_from(blue_edges)

green_line = [
    "Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту",
    "Кловська", "Печерська", "Дружби народів", "Видубичі", "Славутич",
    "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська",
    "Червоний хутір"
]
green_edges = [(green_line[i], green_line[i + 1]) for i in range(len(green_line) - 1)]
metro_graph.add_edges_from(green_edges)

# Додаємо пересадки
metro_graph.add_edge("Театральна", "Золоті ворота")
metro_graph.add_edge("Хрещатик", "Майдан Незалежності")
metro_graph.add_edge("Площа Льва Толстого", "Палац спорту")

# Алгоритм пошуку в глибину (DFS)
def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph.neighbors(start):
        if node not in path:
            newpath = dfs(graph, node, end, path)
            if newpath:
                return newpath
    return None

# Алгоритм пошуку в ширину (BFS)
def bfs(graph, start, end):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        for neighbor in graph.neighbors(node):
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# Визначаємо стартову і кінцеву станції для пошуку
start_station = "Академмістечко"
end_station = "Лісова"

# Виконуємо пошук
dfs_path = dfs(metro_graph, start_station, end_station)
bfs_path = bfs(metro_graph, start_station, end_station)

# Виводимо результати
print(f"Шлях DFS з {start_station} до {end_station}: {dfs_path}")
print(f"Шлях BFS з {start_station} до {end_station}: {bfs_path}")

# Візуалізація графа з шляхами
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(metro_graph, seed=42)
nx.draw(metro_graph, pos, with_labels=True, node_size=50, font_size=8, node_color="skyblue", edge_color="gray")

# Відзначимо шляхи
if dfs_path:
    dfs_edges = list(zip(dfs_path, dfs_path[1:]))
    nx.draw_networkx_edges(metro_graph, pos, edgelist=dfs_edges, edge_color='red', width=2, label='DFS Path')

if bfs_path:
    bfs_edges = list(zip(bfs_path, bfs_path[1:]))
    nx.draw_networkx_edges(metro_graph, pos, edgelist=bfs_edges, edge_color='green', width=2, label='BFS Path')

plt.title("Схема метро Києва з шляхами DFS (червоний) та BFS (зелений)")
plt.legend()
plt.show()
