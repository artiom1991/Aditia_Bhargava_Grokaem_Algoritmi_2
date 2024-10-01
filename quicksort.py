import time
import random


def quicksort_old(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_old(less) + [pivot] + quicksort_old(greater)


def quicksort_new(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        less = [i for i in array if i < pivot]
        greater = [i for i in array if i > pivot]
        return quicksort_new(less) + [pivot] + quicksort_new(greater)


start = time.time()
quicksort_old([i for i in range(1, 1_000)])
end = time.time()
print("Old quicksort time:", end - start)
# RecursionError: maximum recursion depth exceeded

start = time.time()
quicksort_new([i for i in range(1, 1_000)])
end = time.time()
print("New quicksort time:", end - start)

