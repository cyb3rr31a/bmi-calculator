# Define a function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Define a function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    else:
        return "Overweight"

# Get user input for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI and determine BMI category
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

# Print the result
print("Your BMI is:", round(bmi, 2))
print("You are", category)
