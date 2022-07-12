# Год и день рождения А.С.Пушкина (по новому стилю 26 мая 1799)

try:
    if int(input('Введите год рождения А.С.Пушкина: ')) == 1799 and int(input('Введите день рождения А.С.Пушкина: ')) == 26:
        print('Верно')
    else:
        raise Exception()
except:
    print('Неверно')

# 2й более длинный вариант с двумя if

# try:
#     if int(input('Введите год рождения А.С.Пушкина: ')) == 1799:
#         if int(input('Введите день рождения А.С.Пушкина: ')) == 26:
#             print('Верно')
#         else:
#             raise Exception()
#     else:
#         raise Exception()
# except:
#     print('Неверно')