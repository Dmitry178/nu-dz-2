# Викторина "Угадай год рождения известных людей"

import random

# Словарь с годами рождения
data = {'А.С. Пушкина' : 1799, 'М.Ю. Лермонтова' : 1814, 'М.В. Ломоносова' : 1711, 'Пётра I' : 1672,
        'Екатерины Великой' : 1729, 'Николая II' : 1868, 'Михаила Булгакова': 1891, 'Юрия Гагарина': 1934,
        'Брэда Питта' : 1963, 'Анджелины Джоли' : 1975, 'Джеймса Бонда (Шон Коннери)': 1930,
        'Терминатора (Арнольд Шварценеггер) ': 1947, 'Нео (Киану Ривз)': 1967, 'Леонардо Ди Каприо': 1974,
        'Джека Воробья (Джонни Депп)': 1963}

# Имя и год рождения выбирается из словаря случайным образом N раз.
# Могут быть повторения. Для исключения этого, можно с каждой итерацией викторины
# сортировать ключи словаря случайным образом и выбирать первые N записей из словаря (не реализовано)

questions = 5; # количество вопросов

while True:
    # если пользователь ввёл 'да', будет выводиться подсказка года
    prompt = input('Если вам нужна подсказка, введите "да": ').lower() == 'да'

    print()
    correct_answer = 0; # количество правильных ответов

    for i in range(questions):
        try:
            name = key, year = random.choice(list(data.items())) # случайный выбор из словаря (не учтена возможность повторения вопроса)
            user_answer = int(input('Введите год рождения ' + name[0] + (' [' + str(year) + ']' if prompt else '') + ': '))
            if (user_answer == year):
                correct_answer += 1
        except:
            continue

    print()
    print('Викторина завершена')
    print()
    print('Правильных ответов:', correct_answer)
    print('Количество ошибок: ', questions - correct_answer)
    print('Процент правильных ответов:  ', correct_answer * 100 / questions)
    print('Процент неправильных ответов:', 100 - correct_answer * 100 / questions)
    print()

    answ = None
    while True:
        answ = input('Повторить игру (да/нет)? ').lower()
        if answ == 'да' or answ == 'нет':
            break

    if answ == 'нет':
        break

    print()