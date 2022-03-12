import math
from typing import List

data = {
    "START": {
        "A": 6,
        "B": 2,
    },
    "A": {
        "FIN": 1,
    },
    "B": {
        "A": 3,
        "FIN": 5,
    },
    "FIN": {
    },
}
start_node = "START"
end_node = "FIN"

costs = {
    k: dict(
        value=0 if k == start_node else math.inf,
        pending=True
    ) for k in data.keys()
}

current_parents = {}


def get_min_cost_index(node_cost: dict):
    min_node = math.inf
    min_node_name = None
    for node_name, info in node_cost.items():
        if info["pending"] and (info["value"] < min_node):
            min_node_name = node_name
            min_node = info["value"]
    return min_node_name


def update_cost(graph: dict, cost_data: dict, parents: dict, node_name: str):
    node_from: dict = graph[node_name]
    print(node_name)
    for node_name_to, value in node_from.items():
        print(f"\tnode_name_to({node_name_to}): {value}")
        cost_node_to = cost_data[node_name_to]
        temp_cost = cost_data[node_name]["value"] + value
        if temp_cost < cost_node_to["value"]:
            cost_node_to["value"] = temp_cost
            parents[node_name_to] = node_name
    cost_data[node_name]["pending"] = False
    print(costs)
    print()


def get_route(parents: dict, finish_node: str) -> List:
    current_node = finish_node
    route = [finish_node]
    while previous_node := parents.get(current_node):
        route.append(previous_node)
        current_node = previous_node
    route.reverse()
    return route


print(data)
print(costs)
print(get_min_cost_index(costs))
while current_node_name := get_min_cost_index(costs):
    update_cost(data, costs, current_parents, current_node_name)

print(current_parents)
print(' ---> '.join(get_route(current_parents, end_node)))
