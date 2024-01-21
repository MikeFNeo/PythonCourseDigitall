# Input your Wieght and Height
weight_in_kilograms = 75
height_in_meters = 1.80

# Calculate BMI according to the formula - BMI = W / (H*H) and round the result to 2 decimal points
bmi = weight_in_kilograms / (height_in_meters*height_in_meters)
bmi_2 = round(bmi, 2)

print(bmi_2)