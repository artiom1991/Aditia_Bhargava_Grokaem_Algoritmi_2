# Адитья Бхаргава
### Грокаем алгоритмы. Второе издание 2024
![book cover](./images/img.jpg)

## Определения:
> __Алгоритм:__ это набор инструкций для выполнения некоторой
> задачи. В принципе любой фрагмент программного кода можно назвать
> алгоритмом, но в этой книге рассматриваются более интересные темы. 

> __Массивы:__ это структура данных, состоящая из фиксированного количества элементов одного типа, расположенных в 
> непрерывной области памяти. Каждый элемент массива имеет уникальный индекс, который позволяет быстро получать 
> доступ к элементам по их позиции.  
> ![array](./images/array.png)

> __Связанные списки:__ это структура данных, состоящая из узлов, где каждый узел содержит данные и ссылку 
> (или указатель) на следующий узел в последовательности. В отличие от массивов, связанные списки не требуют
> непрерывного выделения памяти и могут динамически изменять свой размер.
> ![list](./images/list.png)

> _Сортировка выбором:_ Самый простой тип сортировки который исполняется за время `O(n*n)` или `O(n^2)`.
> Фактическая скорость выполнения данного алгоритма быстрее почти в 2 раза чем O(n^2) а именно `O((n(n+1))\2)`.
> Сам алгоритм прост. Последовательно проверяется каждый элемент массива и сравнивается со всеми остальными.
> Самый маленький элемент копируется в новый массив. Таким образом формируется новый массив из отсортированных 
> значений по возрастанию из старого массива.
> ![selection-sort](./images/selection_sort.png)

> _Быстрая сортировка:_ Она работает намного быстрее сортировки выбором и часто применяется в реальных программах. 
> Быстрая сортировка также основана на стратегии «разделяй и властвуй». Алгоритм быстрой сортировки работает так: 
> сначала в массиве выбирается элемент, который называется опорным. Далее мы проверяем все элементы списка
> и разделяем их на два массива. В массив слева помещаются элементы меньше опорного, а в массив справа те что больше.
> Время выполнения алгоритма в лучшем случае `O(n * log n)` а в худшем `O(n*n)` или `O(n^2)`
> ![quicksort](./images/quicksort.png)

> __Хеш-таблица:__ Сами по себе таблици реализованы на основе массива, таким образом доступ к 
> определенному элементу таблици осуществляется, как и в массиве со скоростью O(1). При помощи хеш-функции текстовая 
> строка приравнивается в рамках таблици с определенным индексом массива и через это строковое представление 
> мгновенно получает доступ к значению. Они также известны под другими названиями: «ассоциативные массивы»,
> «словари», «отображения», «хеш-карты» или просто «хеши». В Python это словарь.  
> ![hash-table](./images/hash-table.png)

> __Хеш-функция:__ представляет собой функцию, которая получает строку и возвращает число. В научной терминологии
> говорят, что хеш-функция «отображает строки на числа». 
> Проще говоря хеш-функция связывает строки с числами.  
> ![hash-function](./images/hash-function.png) 

> __Коллизия:__ ситуация, когда два или более элемента данных (например, хеш-значения) совпадают, 
> что может привести к ошибкам или неэффективности в обработке информации.  
> Если несколько ключей отображаются на один элемент, в этом элементе создается связанный список.
> ![colision](./images/colision.png)
> Если связанные списки становятся слишком длинными, работа с хеш-таблицей сильно замедляется.
> ![colision](./images/colision_1.png)

> __Рекурсия:__ это вызов функцией самой себя. Когда вы пишете рекурсивную функцию, в ней необходимо указать, в 
> какой момент следует прервать рекурсию. Вот почему каждая рекурсивная функция состоит из двух частей: 
> базового случая и рекурсивного случая. В рекурсивном случае функция вызывает сама себя. В базовом случае
функция себя не вызывает, чтобы предотвратить зацикливание.
> ![recursion](./images/recursion.png)
> >«Циклы могут ускорить работу программы. Рекурсия может ускорить работу программиста. 
> Выбирайте, что важнее в вашей ситуации!»

> __Стек:__ вы не можете обращаться к произвольным элементам стека. Вместо этого поддерживаются
> всего две операции: добавить в стек и извлечение из стека. Стек принадлежит к числу структур
> данных LIFO: Last In, First Out («последним пришел, первым вышел»).
> Когда вы вызываете функцию из другой функции, вызывающая функция приостанавливается в частично 
> завершенном состоянии. Все значения переменных этой функции остаются в памяти.
> ![call-stack](./images/call_stack.png)
> ![stack](./images/stack_img.png)

> __Граф:__ Графы моделируют набор связей и состоят из узлов и ребер.  
> ![graph_2](./images/graph_2.png)  
> Узел может быть напрямую соединен с несколькими другими узлами. Эти узлы называются внутренними или 
> внешними соседями.  
> ![graph](./images/graph.png)

> __Поиск в ширину:__ Поиск в ширину позволяет найти кратчайшее расстояние между двумя объектами. Однако сам 
> термин «кратчайшее расстояние» может иметь много разных значений! 
> ![BFS](./images/BFS.png)  
> Поиск в ширину осуществляется начиная от связей первого уровня, и постепенно двигается от 
> внутреннего кольца связей к внешнему: второму, третьему итд.  
> Поиск в ширину имеет две задачи:
> - найти путь от узла А до узла Б
> - а так ищет самый короткий путь из всех возможных  
> ![deep_search](./images/deep_search.png)
> Связи первого уровня предпочтительнее связей второго уровня, связи второго уровня предпочтительнее связей третьего
> уровня и т. д. Отсюда следует, что поиск по связям второго уровня не должен производиться, пока вы не будете 
> полностью уверены в том, что среди связей первого уровня нет искомого. Связи первого уровня добавляются
> в список поиска раньше связей второго уровня и для операций такого рода существует специальная структура данных, 
> которая называется очередью.

> __Очередь:__ Очередь относится к категории структур данных FIFO: First In, First Out («первым вошел, первым вышел»).
> Вы не можете обращаться к произвольным элементам очереди. Вместо этого поддерживаются всего две операции: 
> постановка в очередь и извлечение из очереди.  
> ![order](./images/order.png)  
> __Реализация алгоритма:__  
> ![deep_search_algoritm](./images/deep_search_algoritm.png)

> __Дерево:__ это разновидность графа. Как и графы, деревья состоят из узлов и ребер.
> У узлов могут быть дочерние узлы, а у дочерних узлов может быть родительский узел.
> В дереве узлы имеют по крайней мере одного родителя. Существует только один узел без родителя — это корневой узел.
> Узлы, не имеющие дочерних узлов, называются листовыми узлами (листьями).
> Так как дерево является разновидностью графа, к нему можно применить алгоритм, работающий с графом.
> ![three](./images/three_2.png)
> Для перебора файлов в каталоге можно воспользоваться поиском в ширину.
> ![three](./images/three_3.png)

>__Алгоритм поиск в ширину:__ Когда он находит папку, эта папка добавляется в очередь для проверки в будущем.  
> ![deep_search_3](./images/deep_search_3.png)  
>__Алгоритм поиска в глубину:__ Поиск в глубину тоже работает с графом и представляет собой алгоритм обхода 
> дерева. При обнаружении папки он сразу заходит в нее, вместо того чтобы добавлять ее в очередь.
> Поиск в глубину не может использоваться для нахождения кратчайшего пути!
> ![deep_search_4](./images/deep_search_4.png)




> __Бинарные деревья:__ Бинарное дерево представляет собой особую разновидность дерева, узлы которого могут
> иметь не более двух дочерних узлов (отсюдаи название). Дочерние узлы традиционно называются левым и правым узлами.
> Важно то, что ни у одного узла не может быть больше двух дочерних узлов. Иногда встречаются термины «левое поддерево»
> и «правое поддерево».
> ![binary_three](./images/binary_three.png)

> __Алгоритм Хаффмана или Алгоритм сжатия:__ Алгоритмы сжатия сокращают количество битов, необходимых для представления каждого символа.
> К примеру используя кодировку ISO-8859-1, один символ занимает 8 бит или 1 байт, однако при помощи алгоритма
> сжатия может потребоваться намного меньше, к примеру 2 бита. Это достигается при помощи создания дерева с новыми
> значениями кодировки. Алгоритм ищет повторяющиеся символы и использует для их представления менее 8 бит. 
> В результате происходит сжатие данных. Код Хаффмана генерирует дерево.
> Пример: сжатие применяется к фразе «paranoid android». Дерево, сгенерированное алгоритмом Хаффмана, выглядит так:
> ![haffman](./images/haffman.png)  
> В алгоритме Хаффмана буквы помещаются только в листовых узлах.
> Для того что бы получить букву необходимо добраться до листового узла, каждый поворот влево добавляет к коду
> 0, а каждый поворот вправо добавляет 1, таким образом формируется код буквы. Так же в правое поддерево 
> помещаются символы, что встречаются чаще, для более быстрого доступа и повышенного сжатия.
> Так как «paranoid android» состоит из 8 символов, а 1 бит хранит в себе два значения `0 и 1`, таким образом
> `2**3 = 8` а это значит что символы из данной строки можно закодировать всего на 3 битах памяти.
> ![binary_three_2](./images/binary_three_2.png)






> __Сбалансированное бинарное дерево (BST):__ Обьеденяет в себе скорость добавления нового элемента в связанного списка,
> а так же быстроту поиска отсортированного массива (как в бинарном поиске).Как и в бинарном дереве, каждый узел имеет 
> до двух дочерних узлов: левый и правый. Но у этого дерева есть одно свойство: значение левого 
> дочернего узла всегда меньше, чем значение родительского узла, а значение правого дочернего узла всегда больше. 
> Более того, все числа в поддереве левого дочернего узла меньше самого узла. Это особое свойство означает, что поиск 
> будет выполняться очень быстро.
> ![BST](./images/BST.png)
> ![BST_1](./images/BST_1.png)
> ![formating_bst](./images/formating_bst.png)

> __Самосбалансированные бинарные деревья:__ АВЛ-деревья сохраняют высоту O(log n). Каждый раз, когда дерево 
> разбалансируется, то есть его высота становится отличной от O(log n), оно корректирует себя. 
> В последнем примере дерево может перебалансироваться и принять следующий вид:
> ![avl](./images/AVL.png)  
> АВЛ-дерево обеспечивает нужную высоту O(log n), которая достигается самобалансировкой и поворотами.
> Допустим есть дерево из 3 узлов. Любой из них может быть корневым.
> ![rotate_1](./images/rotate_1.png)  
> В результате поворота набор узлов смещается, образуя новую конфигурацию. Рассмотрим поворот в замедлении.
> ![rotate_2](./images/rotate_2.png)
> ![rotate_3](./images/rotate_3.png)
> Чтобы дерево знало, когда требуется самобалансировка, оно должно хранить дополнительную информацию. 
> В каждом узле хранится один или два вида информации: значение высоты или значение, которое иногда называют
> коэффициентом балансировки. Этот коэффициент должен быть равен –1, 0 или 1. Коэффициент балансировки сообщает, 
> какой дочерний узел выше и насколько. По коэффициенту балансировки дерево может определить, когда следует 
> проводить перебалансировку. Значение 0 означает, что дерево сбалансировано. Со значениями –1 или 1 тоже все 
> нормально, потому что, напомним, АВЛ-деревья не обязаны быть идеально сбалансированы: разность 1 допустима.
> Но если коэффициент балансировки падает ниже –1 или поднимается выше 1, дерево нуждается в перебалансировке.
> ![rebalance_1](./images/rebalance_1.png)
> ![rebalance_2](./images/rebalance_2.png)
> Вставка сводится к поиску места для вставки узла и добавления указателя, как в связанном списке. 
> Например, если вы захотели вставить 8 в это дерево, необходимо определить, где добавить указатель. Таким образом, 
> вставки тоже выполняются за время O(log n)


## Скорость выполнения алгоритма
| Формула         | Описание                                                                              |
|-----------------|---------------------------------------------------------------------------------------|
| `O(log2 n)`     | Логарифмическое время. Пример: бинарный поиск. Пример: `O(log2 128)` `=` `7 итераций` |
| `O(n)`          | Линейное время. Пример: простой поиск. Пример `O(128)` `=` `128 итераций`             |
| `O(n * log2 n)` | Эффективные алгоритмы сортировки. Пример `O(128 * log2 128)` `=` `896 итераций`       |
| `O(n**2)`       | Медленные алгоритмы сортировки. Пример `O(128 * 128)` `=` `16_384 итераций`           |
| `O(n!)`         | Очень медленные алгоритмы. Пример `O(10!)` `=` `3_628_800 итераций`                   |


## Бинарный поиск:
> Бинарный поиск — это алгоритм который на входе получает отсортированный список элементов. 
> Если элемент, который вы ищете, присутствует в списке, то бинарный поиск возвращает ту позицию, в которой он был найден.
> Алгоритм бинарного поиска состоит из постоянного деления на 2.
> Так же при делении нужно проверять значение больше, меньше или равно искомому, тем самым
> если число больше то берем ту половину деления что больше, если меньше то ту что меньше.  
> ![binary_search](/images/binary_search.png)

> Мы загадали число x которое равняется 8.  
> `x = 8 `  
> __Первая итерация:__ `128:2 = 64 => x < 64 =>`  
> __Вторая итерация:__ `64:2 = 32 => x < 32 =>`  
> __Третья итерация:__ `32:2 = 16 => x < 16 =>`  
> __Четвертая итерация:__ `16:2 = 8 => x == 8`  
> Загаданное число найдено с `4` попытки. 

> В общем случае для списка из n элементов бинарный поиск выполняется за `log`<sub>`2`</sub> `n` шагов, 
> тогда как простой поиск будет выполнен за n шагов.
> Например log<sub>2</sub>128 = 7  
> 2<sup>7</sup> = 128  <=>  log<sub>2</sub>128 = 7
