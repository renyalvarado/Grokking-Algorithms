import collections
import pprint

data = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}


def is_seller(person: str) -> bool:
    return person[-1] == "m"


def search(graph: dict, initial_person: str) -> str:
    person = initial_person
    search_queue = collections.deque()
    searched = []
    for element in graph[person]:
        search_queue.append(element)
    print(search_queue)
    while search_queue:
        person = search_queue.popleft()
        if is_seller(person):
            print("*" * 80)
            return person
        if person not in searched:
            searched.append(person)
            for element in graph[person]:
                search_queue.append(element)
        print("*" * 80)
        print(f"person: {person}")
        print(f"search_queue: {search_queue}")
        print(f"searched: {searched}")
    return None


pprint.pprint(data)
print(f'seller is: {search(data, "you")}')
