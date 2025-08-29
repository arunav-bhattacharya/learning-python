# Boolean datatype
# ================

# A boolean datatype can have 2 values - True or False
# There are 3 operators that works on Boolean - and, or, not

# if-elif-else statement

cars = ['bmw', 'audi', 'tesla', 'hyundai', 'ToYOta', 'honda']

for car in cars:
    if car == 'tesla' or car == 'bmw':
        print(car.upper())
    elif car == 'audi' or car == 'hyundai':
        print(car.title())
    elif car.lower() == 'toyota':
        print(car.lower())
    else:
        print(car)

if "tesla" in cars:
    print(cars.index("tesla"))

