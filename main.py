first = 1
second = 2
third = 3
if first == second == third:
    # если все числа равны между собой выводим 3
    print (3)
elif first == second or second == third or first == third:
    # если хотя бы два из введенных чисел равны между собой выводим 2
    print (2)
else:
    # если равных чисел нет выводим 0
    print (0)
