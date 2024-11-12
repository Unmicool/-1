numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Находим индекс пропущенного элемента (None)
none_index = numbers.index(None)

# Вычисляем сумму всех чисел, кроме пропуска
sum_of_numbers = sum(x for x in numbers if x is not None)

# Количество элементов, кроме пропуска
count_of_numbers = len(numbers)

# Среднее арифметическое
average = sum_of_numbers / count_of_numbers

# Заменяем значение пропущенного элемента на среднее арифметическое
numbers[none_index] = round(average, 2)  # Округляем до двух знаков

# Выводим измененный список
print("Измененный список:", numbers)
