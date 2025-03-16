# write a function for polindrome
def Polindrome(string):
    string = string.replace(" ", '').replace(',', '').replace(':', '').lower()
    newStr = string[::-1]
    count = 0

    if len(string) < 2:
        return True
    
    for i in range(len(string)):
        if string[i] == newStr[i]:
            count += 1

    if len(string) == count:
        return True
    else:
        return False
            

# create instance 

string = 'A man, a plan, a canal: Panama'
print(Polindrome(string))


