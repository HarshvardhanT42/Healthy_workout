def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) based on weight and height.
    
    :param weight: Weight in kilograms
    :param height: Height in meters
    :return: BMI value
    """
    return weight / (height ** 2)

def determine_workout_routine(bmi, age):
    """
    Determines a suitable workout routine based on BMI and age.
    
    :param bmi: Body Mass Index
    :param age: Age of the person
    :return: Suggested workout routine
    """
    if bmi < 18.5:
        return "You are underweight. Focus on strength training and consuming a balanced diet."
    elif 18.5 <= bmi < 24.9:
        if age < 30:
            return "You are at a healthy weight. Incorporate a mix of cardio, strength training, and flexibility exercises."
        elif 30 <= age < 50:
            return "You are at a healthy weight. Focus on moderate cardio, strength training, and flexibility exercises."
        else:
            return "You are at a healthy weight. Prioritize low-impact cardio, strength training, and flexibility exercises."
    elif 25 <= bmi < 29.9:
        if age < 30:
            return "You are overweight. Focus on cardio exercises and incorporate strength training."
        elif 30 <= age < 50:
            return "You are overweight. Incorporate regular cardio, strength training, and monitor your diet."
        else:
            return "You are overweight. Focus on low-impact cardio, strength training, and a balanced diet."
    else:
        if age < 30:
            return "You are obese. Focus on low-impact cardio and consult a fitness professional for a personalized plan."
        elif 30 <= age < 50:
            return "You are obese. Incorporate low-impact cardio and strength training, and consult with a healthcare provider."
        else:
            return "You are obese. Focus on gentle cardio, strength training, and consult with a healthcare provider for a personalized plan."

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        age = int(input("Enter your age: "))

        if weight <= 0 or height <= 0 or age <= 0:
            print("Please enter valid positive values.")
            return

        bmi = calculate_bmi(weight, height)
        routine = determine_workout_routine(bmi, age)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Suggested workout routine: {routine}")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight, height, and age.")

if __name__ == "__main__":
    main()
