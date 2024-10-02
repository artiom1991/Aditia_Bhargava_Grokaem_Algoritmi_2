import time



def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    i1 = 0
    for i in range(len(arr)):
        i1 += len(arr)
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    print("Всего элементов было отсортировано: ", i1)
    return newArr


start = time.time()
selectionSort([i for i in range(0, 1_000)])
end = time.time()
print("Время выполнения алгоритма: ", end - start)


# Теоретическая скорость отработки этого алгоритма O(n*n) или O(n^2)
# В нашем случае это 1_000 * 1_000 или 1_000^2 это равно 1_000_000 операций
# Однако реальная скорость работы немного быстрее, а именно O( (n * (n+1)) / 2 )
# что в результате для 1_000 элементов дает 500500 итераций

