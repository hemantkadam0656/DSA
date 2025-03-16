def Move_Zeros(list):
    n = len(list)
    temp = []

    if n < 2:
        return list
    
    for i in list:
        if i == 0:
            list.remove(i)
            list.append(i)

    print(list) 
    
list = [1,0,2,3,4,0,5,0,6,0]
obj = Move_Zeros(list)


