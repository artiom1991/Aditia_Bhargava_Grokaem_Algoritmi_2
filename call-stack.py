
# В этой программе при помощи рекурсии высчитывается факториал 10
# При помощи вывода в консоль я продемонстрировал работу стека вызова функции
# По принципу последний пришел - первый ушел, начиная с последней вызванной функции
# завершается ее выполнение. Последней вызвалась функция с параметром 1: fact(1) и она же первая завершилась
# вернув значение и начав цепочку завершения всех остальных функций по цепочке с конца.
def fact(x):
    if x == 1:
        print("Current X = ", x)
        return 1
    else:
        res = x * fact(x - 1)
        print("Current X = ", x)
        return res


f = fact(10)
print(f)
