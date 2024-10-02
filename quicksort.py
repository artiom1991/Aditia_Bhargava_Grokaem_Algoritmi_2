import time
import random


def quicksort_old(array):
    if len(array) < 2:  # базовый случай
        return array
    else:               # рекурсивный случай
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_old(less) + [pivot] + quicksort_old(greater)


def quicksort_new(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array) # выбор случайного опорного элемента
        less = [i for i in array if i < pivot]
        greater = [i for i in array if i > pivot]
        return quicksort_new(less) + [pivot] + quicksort_new(greater)



# Если передавать отсортированый список, или слабо отсортированый то это алгоритм работает очень медленно
# В данном случае он отрабатывает за O(n*n) что фактически медленнее чем сортировка выбором
# Проблема в том что опорным элементом выбирается первый элемент списка
start = time.time()
arr_old = quicksort_old([i for i in range(1, 1_000)])
end = time.time()
print("Old quicksort time:", end - start)
# RecursionError: maximum recursion depth exceeded

# Во втором примере случайным образом выбирается опорный элемент, что позволяет алгоритму
# даже в слабо отсортированном списке отработать за максимально короткое время, что приближает алгоритм к O(n * log n)
start = time.time()
arr_new = quicksort_new([i for i in range(1, 1_000)])
end = time.time()
print("New quicksort time:", end - start)

