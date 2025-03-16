def ClosestNum(target,num):
    temp = int(target / num)    # 7 / 2 = 3   -7 / 2 = -3

    n1 =  num * temp # 2 * 3 = 6

    if((target * num) > 0 ):
        n2 = (num * (temp + 1))  # 8 = (2 * (3 + 1) )
    else:
        n2 = (num * (temp - 1)) # -8 = ( 2 * (-3 -1) )
    
    if (abs(target - n1 ) < abs(target - n2)): # 7 - 6 < 7 - 8 = 1 < -1
        return n1
    
    return n2


if __name__ == '__main__':
    target = int(input())       
    num = int(input())
    obj = ClosestNum(target,num) # 7 2
    print(obj)
    