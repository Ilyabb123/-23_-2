numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum_of_numbers_1 = sum(numbers[:4])
sum_of_numbers_2 = sum(numbers[5:])
sum_of_numbers = sum_of_numbers_1 + sum_of_numbers_2
count_of_numbers = len(numbers)
average_of_numbers = round(sum_of_numbers / count_of_numbers, 2)
numbers[4] = average_of_numbers
# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:", numbers)
