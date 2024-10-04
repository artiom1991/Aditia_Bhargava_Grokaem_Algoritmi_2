
# Пример использования рекурсии
# в ней есть базовый случай и рекурсивный случай
def countdown(i):
    print(i)
    if i <= 1:              # Базовый случай
        return
    else:                   # Рекурсивный случай
        countdown(i - 1)

# countdown(10)

def sum(number):
    print("Функция запустилась: ", number)           # порядок запуска функций
    if number <= 1:
        print("!Функция завершилась: ", number)     # порядок завершения выполнения функций
        return number
    else:
        res = number + sum(number - 1)
        print("!Функция завершилась: ", number)      # порядок завершения выполнения функций
        return res

# s = sum(5)
# s = sum(999)
s = sum(1000)
print(s)