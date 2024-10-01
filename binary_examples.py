import time

def usual_search(list, pow):
    start = time.time()
    item = 2**pow
    index = -1
    for el in list:
        index += 1
        if el == item:
            end = time.time()
            print(f"Usual search: 2**{pow}; index={index} duration {end - start}!")
            return index

def binary_search(list, pow):
    start = time.time()
    item = 2**pow
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            end = time.time()
            print(f"Binary search: 2**{pow}; index={mid} duration {end - start}!")
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    end = time.time()
    print(f"Binary search: 2**{pow}; index={None} duration {end - start}!")
    return None
#

my_list = range(1, 4_294_967_296)

for i in range(1, 32):
    binary_search(my_list, i)
    usual_search(my_list, i)






# print("result_idnex:", binary_search(my_list, 16))
# print("result_idnex:", binary_search(my_list, -1))

