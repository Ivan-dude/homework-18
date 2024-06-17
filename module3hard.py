data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
ds = data_structure #сократили для удобства написания кода
s = 0 #переменная счетчик для подсчета кол-ва букв и суммы чисел
def calculate_structure_sum(ds):
        result = []
        for i in ds:
            if isinstance(i, list):  # [] определение вложенного списока и далее выполнение цикла
                for j in i:
                    if isinstance(j, set):  # {1, 2, 3} определение множества и добавление значений в список
                        result.extend(calculate_structure_sum(j))
                result.extend(calculate_structure_sum(i))
            elif isinstance(i, dict):  # {'a': 1, 'b': 2} определение словаря и добавления значений в список
                for j in i:
                    if isinstance(i[j], str):
                        result.extend(calculate_structure_sum(j))
                    if isinstance(i[j], int):
                        result.extend(calculate_structure_sum(j))
                result.extend(calculate_structure_sum(list(i.values())))
            elif isinstance(i, tuple):  # () определение кортежа и доб. значений в список
                result.extend(calculate_structure_sum(list(i)))
            elif isinstance(i, str):
                result.extend(i)
            elif isinstance(i, int):
                result.append(i)
        return result
result = calculate_structure_sum(ds) # вызов функции для просмотра и проверки получившегося списка

for letter in result: # цикл для подсчета кол-ва элементов типа str
    if isinstance(letter, str):
        s += 1
sum_num = sum([int(num) for num in result if type(num) == int]) #подсчет суммы элементов типа int
total_sum = s + sum_num
print('Получаем значение: ', total_sum) # вывод итогового  значения
