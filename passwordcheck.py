def password_strength(password):
    """
    Program to check strength of the input password parameter :
    password(str): input password
    return:
    output (str) : Weak or Average or Strong
    """
    special_chars = list("@#$%^&*")
    isdigit_there = any(char.isdigit() for char in password)
    isupper_there = any(char.isupper() for char in password)
    isspchar_there = any(char.isdigit() for char in password)
    check_lower = any(char.islower() for char in password)

    all_true = all([isdigit_there, isupper_there, isspchar_there, check_lower])
    if len(password) < 6:
        return "Weak"
    elif len(password) >= 8 and all_true:
        return "Strong"
    else:
        return "Average"


input_password = input("Create Password :")
strength = password_strength(input_password)
print("")
print("YOur Password is {} !!".format(strength))
