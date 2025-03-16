def RightAngledTrianglewithNumbers(n):
    list =[]
    for i in range(1,n+1):
        list.append(str(f"{i}"* i))

    return list

n = 5
print(RightAngledTrianglewithNumbers(n))