from math import inf
green = yellow = red = 1.0


def load():
    global green, yellow, red
    print("Podaj koszt przejazdu jednego metra po nawierzchni:")
    while True:
        try:
            green = float(input(" Zielonej: ").replace(",", "."))
            yellow = float(input(" Zoltej: ").replace(",", "."))
            red = float(input(" Czerwonej: ").replace(",", "."))
            if green >= 0 and yellow >= 0 and red >= 0:
                break
            print("Koszt nie moze byc ujemny!")
        except ValueError:
            print("Koszt musi być liczbą!")


def make_hangar(g, y, r):
    warehouse = {"a": {"c": g * 10, "d": y * 2},
                 "b": {"g": y * 12.3, "h": r * 3.3, "j": g * 7.2},
                 "c": {"a": g * 10, "f": g * 4.5, "j": r * 7.8},
                 "d": {"a": y * 2, "e": r * 6.8, "f": y * 7.5},
                 "e": {"d": r * 6.8, "f": g * 3.5, "g": r * 2},
                 "f": {"c": g * 4.5, "d": y * 7.5, "e": g * 3.5, "i": y * 4.2},
                 "g": {"b": y * 12.3, "e": r * 2, "h": r * 1.3},
                 "h": {"b": r * 3.3, "g": r * 1.3, "i": g * 3.7},
                 "i": {"f": y * 4.2, "h": g * 3.7, "j": y * 1.7},
                 "j": {"b": g * 7.2, "c": r * 7.8, "i": y * 1.7}}
    return warehouse


def set_min(graph, start, end):
    shortest_distance = {node: inf for node in graph}
    shortest_distance[start] = 0

    while graph:
        nearest = None

        for node in graph:
            if nearest is None:
                nearest = node
            elif shortest_distance[node] < shortest_distance[nearest]:
                nearest = node

        for child_node, cost in graph[nearest].items():
            if cost + shortest_distance[nearest] < shortest_distance[child_node]:
                shortest_distance[child_node] = cost + shortest_distance[nearest]

        if nearest == end:
            break

        graph.pop(nearest)

    print(f"Najkrotsza droga wymaga {round(shortest_distance[end], 3)} energii")


load()
hangar = make_hangar(green, yellow, red)
set_min(hangar, "a", "b")
