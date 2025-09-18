# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

def print_names():
 return '\n'.join(names)

names = ['Оля', 'Петя', 'Вася', 'Маша']
print(print_names(),'\n')

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4
def calc_letters():
     for letters in names:
          res = len(letters)
          print(letters,":",res)

names_1 = ['Оля', 'Петя', 'Вася', 'Маша']
calc_letters()
print()

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

# is_male = {
#     'Оля': False,
#     'Петя': True,
#     'Вася': True,
#     'Маша': False,
# }

def make_dict():
    is_male = {}
    for name in names_2:
        if name == 'Оля' or name == 'Маша':
            is_male[name] = False
        else:
            is_male[name] = True
    return is_male

names_2 = ['Оля', 'Петя', 'Вася', 'Маша']
print(make_dict(),'\n')

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

def calc_groups():
 print('Всего',len(groups),'группы')
 for group in range(len(groups)):
        count_pupils = 0
        for pupils in range(len(groups[group])):
            count_pupils += 1
        print('Группа',(group + 1),':',count_pupils,'ученика')

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
calc_groups()
print()

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

def enumerate_pupils():
    for group in range(len(groups)):
       print('Группа', (group + 1), ':', ', '.join(groups[group]))


groups_1 = [
        ['Вася', 'Маша'],
        ['Вася', 'Маша', 'Саша', 'Женя'],
        ['Оля', 'Петя', 'Гриша'],
    ]
enumerate_pupils()