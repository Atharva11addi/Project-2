def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")

    # Input weight and height from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify BMI
    category = classify_bmi(bmi)

    # Display results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
