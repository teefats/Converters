
import math
# print("Welcome to the MPH to KMH")
# print()
# def convert():
#     mph = float(input("Please enter a value in mph"))
#     kmh = round((mph * 1.609344), 2)
#     print(f'{mph}mph is {kmh} kmh.')

# convert()


print("Welcome to the temperature coverter")
print()
def convert_temp():
    unit = input("What unit do you want to convert?")
    if unit == "celsius":
        celsius = int(input("Please enter the temperature you want to convert"))
        farenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        print(f'{celsius} celsius is {farenheit}f.')
        print(f'{celsius} celsius is {kelvin}K.')
    elif unit == "farenheit":
        farenheit = int(input("Please enter the temperature you want to convert"))
        celsius = round(((farenheit - 32) * 5/9), 2)
        kelvin = round((((farenheit - 32) * 5/9) + 273.15), 2)
        print(f'{farenheit} farenheit is {celsius}f.')
        print(f'{farenheit} farenheit is {kelvin}K.')
    elif unit == "kelvin":
        kelvin = int(input("Please enter the temperature you want to convert"))
        farenheit = round((((kelvin - 273.15) * 9/5) +32), 2)
        celsius = round((kelvin -273.15), 2)
        print(f'{kelvin} kelvin is {celsius}c.')
        print(f'{kelvin} kelvin is {farenheit}f.')
    else:
        print("Please enter the unit you want to convert")

convert_temp()