from datetime import datetime

def calculate_age(birthdate: str):
    # Convert the birthdate string to a datetime object
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    
    # Get the current date
    today = datetime.today()
    
    # Calculate the age
    age = today.year - birthdate.year
    
    # Adjust age if the birthday hasn't occurred yet this year
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1
    
    return age

# Example usage
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
age = calculate_age(birthdate)
print(f"You are {age} years old.")
