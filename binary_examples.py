import time


def usual_search(list, pow):
    start = time.time()
    item = 2**pow
    index = -1
    i = 0
    for el in list:
        i += 1
        index += 1
        if el == item:
            end = time.time()
            print(f"Usual search: 2**{pow}; iteration={i}; index={index}; duration={end - start};")
            return index

def binary_search(list, pow):
    start = time.time()
    item = 2**pow
    low = 0
    high = len(list) - 1
    i = 0
    while low <= high:
        i += 1
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            end = time.time()
            print(f"Binary search: 2**{pow}; iteration={i}; index={mid}; duration={end - start};")
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

print("Binary search:")
for i in range(1, 32):
    binary_search(my_list, i)

print("Usual search:")
for i in range(1, 32):
    usual_search(my_list, i)

