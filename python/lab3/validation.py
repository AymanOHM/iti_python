def validate_name(name: str):
    if name and name.replace(" ", "").isalpha():
        return True
    return False

# this is simple validation, you can enhance it
# further by checking for text before @ and after .
def validate_email(email: str):
    if email and email.count('@') == 1 and email.count('.') > 0:
        return True
    return False

def validate_password(password: str):
    if password and len(password) >= 8:
        return True
    return False

def validate_phone(phone: str):

    for char in [" ", "-", "(", ")", "+"]:
        phone = phone.replace(char, "")

    if phone and phone.isdigit() and \
        (len(phone) == 11 or (len(phone) == 12 and phone.startswith('2'))):
        return True
    return False

def validate_date(date: str):
    try:
        day, month, year = map(int, date.split("/"))
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 1900:
            return True
    except:
        pass
    return False

def validate_user(data: dict) -> dict:
    return {
        'name' : validate_name(data['name']),
        'email' : validate_email(data['email']),
        'password' : validate_password(data['password']),
        'phone' : validate_phone(data['phone'])
    }

def validate_project(data: dict) -> dict:
    return {
        'name' : validate_name(data['name']),
        'details' : bool(data['details']),
        'target' : data['target'].isdigit(),
        'start_date' : validate_date(data['start_date']),
        'end_date' : validate_date(data['end_date']),
        'status' : bool(data['status'])
    }