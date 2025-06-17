def sum_of_lengths(strings):
    total_length = sum(len(s) for s in strings)
    return total_length
words = ["Hello", "world", "I'm", "Dante", "!!"]
result = sum_of_lengths(words)
print(f"Сумма длин всех строк: {result}")