from collections import  deque


graph = {}
graph["you"] = ["Alisa", "Bob", "Cler"]
graph["Bob"] = ["Anudj", "Peggy"]
graph["Alisa"] = ["Peggy"]
graph["Cler"] = ["Tom", "Jonny"]
graph["Anudj"] = []
graph["Peggy"] = []
graph["Tom"] = []
graph["Jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a saller !")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(person):
    return person == "Jonny"

search("you")