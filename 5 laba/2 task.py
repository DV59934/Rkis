def SumAndMul(numbers):
    positive_sum = sum(x for x in numbers if x > 0)

    min_num = min(numbers)
    max_num  = max(numbers)
    min_index = numbers.index(min_num)
    max_index = numbers.index(max_num)
    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    product = 1
    for num in numbers[start:end]:
        product *= num
    return positive_sum, product

numbers = [5, -3, -9, 1, 6, 2, 8]
sum_pos, product_between = SumAndMul(numbers)
print("Сумма положительных: ", sum_pos)
print("Произведение между min и max: ", product_between)