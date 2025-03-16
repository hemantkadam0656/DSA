def PyramidPattern(n):
    list = []
    for i in range(n):
        list.append(" " * ( i ) + '*' *(n - i) + '*' * (n-i -1) +" " * (i))
    
    return list
    
n = 5
print(PyramidPattern(n))

