A = ["abc", "ab", "bc", "ccc", "cbc", "а"]
C = "c"

count = 0

for a in A:
    if len(a) > 1 and a[0] == C and a[-1] == C:
        count += 1
print("Найдено количесвто элементов:", count)