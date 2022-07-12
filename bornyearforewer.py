# Год рождения А.С.Пушкина (по новому стилю 26 мая 1799)

while True:
    try:
        if int(input('Введите год рождения А.С.Пушкина: ')) == 1799:
            break
        else:
            raise Exception()
    except:
        print('Неверно')
        print()

print('Верно')