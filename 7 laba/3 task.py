numbers = [-16, 4, 8, -12, -1, 13, 66]
result = []
for num in numbers:
    if 10 <= num <= 99:
        result.append(num)
result.sort()
print(f"Двузначные положительные числа): {result}")