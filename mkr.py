# Задаємо масив
array = [[1,6,7], [7,2,9], [1,2,4]]

# Шукаємо середнє значення в кожному рядку заданого масиву 
def find_average(row):
    return sum(row) / len(row)

# Сортуємо рядки масиво за зростанням середнього значення
def sort_array(array):
    return sorted(array, key=find_average)

# Вводимо змінну для виконаної функції       
sorted_array = sort_array(array)

# Виводимо відсортований масив
print(sorted_array)