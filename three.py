from os import listdir
from os.path import isfile, join
from collections import deque

# поиск в ширину
def printnames_base(start_dir):
    search_queue = deque()                      # создает очередь для проверки дерева deque([])
    search_queue.append(start_dir)              # помещает корневой адрес для проверки в очередь deque(["./images"])
    while search_queue:                         # перебирает элементы очереди deque(['./images'])
        dir = search_queue.popleft()            # удаляет первый элемент очереди
        for file in sorted(listdir(dir)):       # перебирает список дочерних элементов
            fullpath = join(dir, file)          # получает полный путь к дочернему элементу ./images\three_2.png
            if isfile(fullpath):                # проверяет, является ли элемент файлом или нет
                print(file)
            else:
                search_queue.append(fullpath)   # если путь является папкой, то помещает его в конец очереди search_queue


printnames_base("./images")                     # "./images" является корневым узлом

print("____________________________")

# поиск в глубину
def printnames(dir):
    for file in sorted(listdir(dir)):           # перебирает список дочерних элементов
        fullpath = join(dir, file)              # получает полный путь к дочернему элементу ./images\three_2.png
        if isfile(fullpath):                    # проверяет, является ли элемент файлом или нет
            print(file)
        else:                                   # если путь является папкой, то рекурсивно добавляется в стек вызовов новый вызов этой же функции но с новым адресом
            printnames(fullpath)


printnames("./images")