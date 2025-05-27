n = int(input("Введите число n: "))
sum_nums = 0
for i in range(1, n + 1):
    sum_nums += i
print(f"Сумма чисел от 1 до {n}(включительно) = {sum_nums}")