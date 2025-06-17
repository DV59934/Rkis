numbers = [5, 7, -4, 3, -11, 1]
first_positive = None
for num in numbers:
    if num > 0:
        first_positive = num
        break

last_negative = None
for num in reversed(numbers):
    if num < 0:
        last_negative = num
        break
print(f"Первый положительный элемент: {first_positive}")
print(f"Последний отрицательный элемент: {last_negative}")