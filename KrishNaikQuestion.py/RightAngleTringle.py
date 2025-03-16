def RightAngleTringle(n):
    list = []
    for i in range(n):
        list.append( " " * (n - (i + 1)))
    
    return list


n = 5
print(RightAngleTringle(n))