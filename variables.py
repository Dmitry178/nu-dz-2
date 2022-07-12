# карточка автомобиля

name = "Hyundai Sonata"     # марка автомобиля
year = 2019                 # год выпуска
engine_vol = 2.5            # объём двигателя (л)
engine_type = "бензин"      # тип двигателя
four_wheel = True           # полный привод
mileage = 50204             # пробег (км)
new = False                 # новая (False - с пробегом)

print('Марка автомобиля:   ', name, ' (', type(name), ')', sep='')
print('Год выпуска:        ', year, ' (', type(year), ')', sep='')
print('Объём двигателя, л: ', engine_vol, ' (', type(engine_vol), ')', sep='')
print('Тип двигателя:      ', engine_type, ' (', type(engine_type), ')', sep='')
print('Полный привод:      ', four_wheel, ' (', type(four_wheel), ')', sep='')
print('Пробег, км:         ', mileage, ' (', type(mileage), ')', sep='')
print('Новая:              ', new, ' (', type(new), ')', sep='')