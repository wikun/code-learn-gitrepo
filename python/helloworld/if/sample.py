cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.lower())

age_0,age_1 = 22,18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

vegetables = ['mushrooms','onions','carrot']
print('onions' in vegetables)
print('onions' not in vegetables)

game_active = True
