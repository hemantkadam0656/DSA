def PasswordStrength(password):
    if len(password)< 8 :
        print(1)
        return False
    if any(char.islower() for char in password):
        print(2)
        return False
    if any(char.isupper() for char in password):
        print(3)
        return False 
    if any( char in '@!+=-_#&*' for char in password ):
        print(4)
        return False
    
    return True



if __name__ == "__main__":
    password = 'Hemantkadam@'
    print(PasswordStrength(password))
