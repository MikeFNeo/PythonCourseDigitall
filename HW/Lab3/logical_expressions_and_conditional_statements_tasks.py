# logical_expressions_and_conditional_statements_tasks.py

# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes a number as input and checks if it is positive, negative, or zero.
"""

### Your code here

# # Input variables
# number_str = input ('Enter a number: ')
# number_float = float (number_str)

# # Check number
# if number_float < 0:
#     print (f'Number {number_float} is negative')
# elif number_float > 0:
#     print (f'Number {number_float} is positive')
# else:
#     print (f'Number {number_float} is 0\n\n')

### EXPECTED OUTPUT:
# "Enter a number: -2.45"
# "Number -2.45 is negative."


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program to check whether a year input by the user is a leap year or not. Use the rule for Gregorian calendar:
    Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
    For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
"""

### Your code here

# # Input variables
# year_str = input ('Enter a year: ')
# year_int = int (year_str)

# # Check leap year
# if year_int % 4 != 0 or (year_int % 100 == 0 and year_int % 400 != 0):
#     print (f'{year_int} is not a leap year')
# else:
#     print (f'{year_int} is a leap year')

### EXPECTED OUTPUT:
# Enter a year: 2024
# 2024 is a leap year

# Enter a year: 2050
# 2050 is not leap year.


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Develop a simple temperature converter program that converts temperatures from Fahrenheit to Celsius and vice versa based on user choice. Make a user-friendly interface as given in EXPECTED OUTPUT:.

    Temperature conversions use the following formulas:
    Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
    Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
"""

### Your code here

# # UI creation
# print (f'{"Fahrenheit/Celsius Converter ":*^50}')
# print (f'{"# 1 => Convert to Fahrenheit": <49}#')
# print (f'{"# 2 => Convert to Celsius": <49}#')
# print (f'{"*":*^50}')

# # Input variables
# choice_num = int (input ('Enter your choice [1/2]: '))
# temp_num = 0.0

# # Selection and conversion logic
# if choice_num == 1:
#     temp_num = round (float (input ('Enter temperature in C: ')), 1)
#     print(f'{temp_num}C = {(temp_num * (9/5)) + 32}F')
# elif choice_num == 2:
#     temp_num = round (float (input ('Enter temperature in F: ')), 1)
#     print(f'{temp_num}F = {(temp_num - 32) * (9/5)}C')
# else:
#     choice_num = int (input ('Wrong Input!\n\nPlease Enter your choice [1/2]: '))



### EXPECTED OUTPUT:
# **********Fahrenheit/Celsius Converter ***********
# # 1 => Convert to Fahrenheit                     #
# # 2 => Convert to Celsius                        #
# **************************************************
# Enter your choice [1/2]: 1
# Enter temperature in C: 20
# 20.0C = 68.0F


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Write a Body mass index (BMI) calculator program, which asks the user for:
    weight in kilograms
    height in meters

    Calculate the BMI = W / (H*H)
    where:
    W = weight in kilograms
    H = height in meters

    Display to the user the BMI and basic category, using next table:

    | ------------------------------- | ----------- |
    | category                        | BMI         |
    | ------------------------------- | ----------- |
    | Underweight (Severe thinness)   | < 16.0      |
    | Underweight (Moderate thinness) | 16.0 - 16.9 |
    | Underweight (Mild thinness)     | 17.0 - 18.4 |
    | Normal range                    | 18.5 - 24.9 |
    | Overweight (Pre-obese)          | 25.0 - 29.9 |
    | Obese (Class I)                 | 30.0 - 34.9 |
    | Obese (Class II)                | 35.0 - 39.9 |
    | Obese (Class III)               | ≥ 40.0      |
    | ------------------------------- | ----------- |
"""

# ### Your code here

# # Input variables
# weight_in_kilos = float (input ('Enter weight in kilograms: '))
# height_in_meters = float (input ('Enter height in meters: '))

# # BMI calculation and Categorization logic
# bmi = weight_in_kilos / (height_in_meters*height_in_meters)
# bmi_2 = round(bmi, 2)

# if bmi_2 < 16.0:
#     print (f'Your BMI = {bmi_2}, Category: Underweight (Severe thinness)')
# elif 16.0 <= bmi_2 <= 16.9:
#     print (f'Your BMI = {bmi_2}, Category: Underweight (Moderate thinness)')
# elif 17.0 <= bmi_2 <= 18.4:
#     print (f'Your BMI = {bmi_2}, Category: Underweight (Mild thinness)')
# elif 18.5 <= bmi_2 <= 24.9:
#     print (f'Your BMI = {bmi_2}, Category: Normal range')
# elif 25.0 <= bmi_2 <= 29.9:
#     print (f'Your BMI = {bmi_2}, Category: Overweight (Pre-obese)')
# elif 30.0 <= bmi_2 <= 34.9:
#     print (f'Your BMI = {bmi_2}, Category: Obese (Class I)')
# elif 35.0 <= bmi_2 <= 39.9:
#     print (f'Your BMI = {bmi_2}, Category: Obese (Class II)')
# else:
#     print (f'Your BMI = {bmi_2}, Category: Obese (Class III)')


### EXPECTED OUTPUT:
# Enter weight in kilograms: 92
# Enter height in meters: 1.78
# Your BMI = 29.04, Category: Overweight (Pre-obese)