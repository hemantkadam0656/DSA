def Rectanguler_Patter(n,m):
    list = []
    for i in range(n):
        list.append("*" * m)
    
    return list


n = 3
m = 2
print(Rectanguler_Patter(n,m))
