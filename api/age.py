from datetime import datetime

def handler(request):
    birthdate = request.args.get('birthdate', '')
    
    if not birthdate:
        return {"statusCode": 400, "body": "Please provide a birthdate in YYYY-MM-DD format."}
    
    # Calculate age
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birthdate.year
    
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1
    
    return {
        "statusCode": 200,
        "body": f"You are {age} years old."
    }
