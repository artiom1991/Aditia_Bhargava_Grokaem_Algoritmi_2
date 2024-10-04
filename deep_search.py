from collections import deque

graph = {
    "you": ["Alisa", "Bob", "Cler"],
    "Bob": ["Anudj", "Peggy"],
    "Alisa": ["Peggy"],
    "Cler": ["Tom", "Jonny"],
    "Anudj": [],
    "Peggy": [],
    "Tom": [],
    "Jonny": [],
    "Marshal": []
}


def search(name, seller_list):
    search_queue = deque()                              # создает пустую очередь ([])
    search_queue += graph[name]                         # добавляет в очередь список связей к примеру (["Alisa", "Bob", "Cler"])
    searched = []                                       # хранит список проверенных зависимостей чтобы не зациклить поиск.
    while search_queue:                                 # отрабатывает пока очередь не пуста
        person = search_queue.popleft()                 # удаляет первый элемент очереди
        if not person in searched:                      # фильтрует связи чтобы не проверять одну и туже связь 2 или более раза
            if person_is_seller(person, seller_list):
                print(person + " is a saller !")
                return True
            else:
                search_queue += graph[person]           # добавляет в очередь связи следующего уровня
                searched.append(person)                 # добавляет имя в список проверенных связей searched чтобы не зациклить проверку
    print("No sallers!")
    return False


def person_is_seller(person, seller_list):
    if person in seller_list:                   # проверяет связь, и если она есть в списке saller_list возвращает имя
        return person
    return False

sellers = ["Cler", "Jonny", "Peggy", "Marshal"] # Cler первый уровень связей
search("you", sellers)

sellers = ["Peggy", "Jonny", "Marshal"] # Peggy второй уровень связей
search("you", sellers)

sellers = ["Jonny", "Marshal"]  # Jonny третий уровень связей
search("you", sellers)

sellers = ["Marshal"]  # No sallers!  хоть Marshal является продавцом, но он ни входит ни в один уровень связей!
search("you", sellers)



