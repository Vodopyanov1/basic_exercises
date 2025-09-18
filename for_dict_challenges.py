# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

def calc_names():
    name_from_dict = []
    for i in students:
        for j in i.values():
            name_from_dict.append(j)

    name_counts = {}
    for name in name_from_dict:
        if name in name_counts:
            name_counts[name] += 1
        else:
             name_counts[name] = 1

    for name, count in name_counts.items():
        print(name,':', count)

students = [
        {'firstn_name': 'Вася'},
        {'first_name': 'Петя'},
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Петя'},
    ]
calc_names()
print()

# Задание 2
# Дан список учеников, нужно вывести самое часто повторяющееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
def common_name():
    list_values =[]
    for dicts in students_1:
       for names in dicts.values():
            list_values.append(names)

    max_common = 0
    comm_name =''
    for pupil_name in list_values:
        a = list_values.count(pupil_name)
        if a > max_common:
            max_common = a
            comm_name = pupil_name
    return comm_name

students_1 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},

]
print('Самое частое имя среди учеников:',common_name(),'\n')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша
def calc_any_groups():
   for lists in range(len(school_students)):
        max_quantity = 0
        string_for_name = ''
        for dicts in school_students[lists]:
            if school_students[lists].count(dicts) > max_quantity:
                 max_quantity = school_students[lists].count(dicts)
                 string_for_name = dicts.values()
   print('Самое частое имя в классе',(lists + 1),':',' '.join(string_for_name))

school_students = [
    [  # это – первый класс
 {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
 {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
 {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
calc_any_groups()
print()

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

def calc_male():
   for i in school:
       count_boys = 0
       count_girls = 0
       for j in i['students']:
           if is_male.get(j['first_name'])==False:
                count_girls += 1
           if is_male.get(j['first_name'])==True:
                count_boys += 1
           if count_boys + count_girls == len(i['students']):
              print('В классе', i['class'],count_girls,'девочки',count_boys,'мальчики')


school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
 'Олег': True,
 'Маша': False,
 'Оля': False,
 'Миша': True,
 'Даша': False,
}
calc_male()
print()

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

def calc_max_male():
    school_values = [list(value.values()) for value in school_1]
    count_genders_in_class = {}

    for lists in school_values:
        for data in lists:
            if isinstance(data, str):
                class_name = data
                count_genders_in_class[class_name] = [{'boys': 0, 'girls': 0}]
            else:
                students_count = len(data)
                key_name = list(data[0].keys())[0]
                student_names = [data[i][key_name] for i in range(students_count)]
                for student_name in student_names:
                    if is_male[student_name]:
                        count_genders_in_class[class_name][0]['boys'] += 1
                    else:
                        count_genders_in_class[class_name][0]['girls'] += 1
    keys = list(count_genders_in_class.keys())
    for index, key in enumerate(keys):
         if count_genders_in_class[key][0]['boys'] > count_genders_in_class[keys[index - 1]][0]['boys']:
              print(f"Больше всего мальчиков в классе {key}")
         else:
              print(f"Больше всего мальчиков в классе {keys[index- 1]}")

         if count_genders_in_class[key][0]['girls'] > count_genders_in_class[keys[index - 1]][0]['girls']:
             print(f"Больше всего девочек в классе {key}")
         else:
            print(f"Больше всего девочек в классе {keys[index - 1]}")
         break

school_1 = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male_1 = {
 'Маша': False,
 'Оля': False,
 'Олег': True,
 'Миша': True,
}
calc_max_male()
