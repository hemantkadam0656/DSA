def isPolindrome(s):
    s = s.lower()
    n = len(s)

    if n < 2:
        return True
    elif s[0] == s[n-1]:
        return isPolindrome(s[1:n-1])
    else:
        return False
    

if __name__ == '__main__':
    string = 'Madam'
    obj = isPolindrome(string)
    print(obj)