import copy
from tabulate import tabulate

COSTS = [i for i in range(1, 5)]
NULL_COST = (0, [],)


class Grid:
    def __init__(self, costs, headers_items, items, debug=False):
        self.costs = costs
        self.headers_items = headers_items
        self.items = items
        self.grid_full_cost = [
            [NULL_COST for _ in costs] for _ in items
        ]
        self.debug = debug

    def __str__(self):
        header_costs = [""] + self.costs
        new_grid_info = [
            [self.items[i][0] + f" ({i})"] + row_grid
            for i, row_grid in enumerate(self.grid_full_cost)
        ]
        return tabulate(new_grid_info, header_costs, tablefmt="fancy_grid")

    def get_grid_info(self, index_element_, index_weight):
        if index_element_ < 0 or index_weight < 0:
            return copy.copy(NULL_COST)
        return self.grid_full_cost[index_element_][index_weight]

    def process_cell(self, index_item, index_weight):
        item_name, item_weight, item_cost = self.items[index_item]
        weight = self.costs[index_weight]
        if self.debug:
            print(f"item_weight: {item_weight}, item_cost: {item_cost}, index_weight: {index_weight}, weight: {weight}")
        diff_weight = weight - item_weight
        previous_cost, previous_items = self.get_grid_info(index_item - 1, index_weight)
        if diff_weight < 0:
            final_info = (previous_cost, previous_items,)
        else:
            diff_cost, diff_items = self.get_grid_info(index_item - 1, diff_weight - 1)
            temp_cost = item_cost + diff_cost
            if temp_cost > previous_cost:
                final_info = (temp_cost, diff_items + [item_name],)
            else:
                final_info = (previous_cost, previous_items,)
        self.grid_full_cost[index_item][index_weight] = final_info

    def process_row(self, index_row):
        for index_cost, _ in enumerate(self.costs):
            if self.debug:
                print(f"index_element, index_cost: {index_row, index_cost}")
            self.process_cell(index_row, index_cost)

    def process_full(self):
        for index_element, _ in enumerate(self.items):
            self.process_row(index_element)
            if self.debug:
                print(self)


headers_items_grid = ["item", "weight", "cost"]

items_grid_01 = [
    ("guitar", 1, 1500,),
    ("stereo", 4, 3000,),
    ("laptop", 3, 2000,),
]
grid01 = Grid(COSTS, headers_items_grid, items_grid_01)
print(grid01)
grid01.process_full()
print(grid01)
print("*" * 80)

items_grid_02 = [
    ("stereo", 4, 3000,),
    ("laptop", 3, 2000,),
    ("guitar", 1, 1500,),
]
grid02 = Grid(COSTS, headers_items_grid, items_grid_02)
print(grid02)
grid02.process_full()
print(grid02)
print("*" * 80)

items_grid_03 = [
    ("guitar", 1, 1500,),
    ("stereo", 4, 3000,),
    ("laptop", 3, 2000,),
    ("iphone", 1, 2000,),
]
grid03 = Grid(COSTS, headers_items_grid, items_grid_03)
print(grid03)
grid03.process_full()
print(grid03)
print("*" * 80)

items_grid_04 = [
    ("guitar", 1, 1500,),
    ("stereo", 4, 3000,),
    ("laptop", 3, 2000,),
    ("iphone", 1, 2000,),
    ("mp3", 1, 1000,),
]
grid04 = Grid(COSTS, headers_items_grid, items_grid_04)
print(grid04)
grid04.process_full()
print(grid04)
print("*" * 80)

items_camping = [
    ("water", 3, 10,),
    ("book", 1, 3,),
    ("food", 2, 9,),
    ("jacket", 2, 5,),
    ("camera", 1, 6,),
]
cost_camping = [i for i in range(1, 7)]
grid_camping = Grid(cost_camping, headers_items_grid, items_camping)
print(grid_camping)
grid_camping.process_full()
print(grid_camping)
print("*" * 80)
