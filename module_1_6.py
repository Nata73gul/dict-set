# Словари

my_dict = {'Eva': 2018, 'Veny': 2022, 'Iriska': 2019, 'Izym': 2020}
print('Список:', my_dict)
print('Год рождения:', my_dict['Eva'])
print(my_dict.get('Knopa', 'Отсутствует в списке'))
my_dict.update({'Berta': 2020, 'Dusy': 2024})
print(my_dict)
a = my_dict.pop('Izym')
print('Удаленное значение:', a)
print('Измененный список:', my_dict)

# Множества

my_set = {3, 3, 3, 2, 2, 2, 7, 7, 7, 'orange', 'banana', 'banana', (4, 5, 6, 7, 8, 9)}
print('set:', my_set)
my_set.add(4.9)
my_set.add(True)
my_set.discard(9)  # нет ошибки, если не найден элемент
my_set.remove((4, 5, 6, 7, 8, 9))
print('Modified set:', my_set)
