# Матричный калькулятор
## Описание
Матричный калькулятор вычисляет значение от выражения с произвольным количеством матриц. При использовании матриц первого порядка работает как обычный калькулятор. В качестве коэффициентов матрицы можно использовать целые числа, десятичные и обыкновенные дроби. Поддерживаются операции сложения, вычитания, умножения, деления, возведения в целую степень, умножения на скаляр и прибавления скаляра (равносильно прибавлению скалярной матрицы).
## Использование
1. Скопируйте этот проект
2. Запустите файл `src/main.py` в интерпретаторе языка Python3
3. Введите выражение с переменными
4. Для каждой используемой переменной введите значение-матрицу, после ввода матрицы вводите пустую строку
5. Получите результат
## Примеры
### Преобразование матрицы линейного оператора при переходе к новому базису
~~~
Input expression:
P^-1*A*P

Input P:
-1 -2 -3  0
 0 -1 -1  1
 0  0  0  1
 1  1  1  0

Input A:
-2  0  0  1
 1 -4  0  1
 0  0 -4  0
 0 -1  1 -3

Result:
-3  1  0  0
 0 -3  1  0
 0  0 -3  0
 0  0  0 -4
~~~
### Подстановка матрицы в ее характеристический многочлен
~~~
Input expression:
(A+4)*(A+3)^3

Input A:
-2  0  0  1
 1 -4  0  1
 0  0 -4  0
 0 -1  1 -3

Result:
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
~~~
