def hallowSquare(n):
    list = []
    for i in range(n):
        if i == 0 or i == n - 1:
            list.append(n * '*')
        else:
            list.append('*' + " "* (n-2) + "*")
    
    return list

n = 7
print(hallowSquare(n))
