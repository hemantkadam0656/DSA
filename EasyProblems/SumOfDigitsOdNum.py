def SumOfDigitsOdNum(num):
    sum = 0 
    if num == 0:
        return 0
    
    while (num != 0):
        n = num % 10 
        sum += n

        num //= 10

    return sum
    
if __name__ == '__main__':
    num = 123456789123456789123422
    print(SumOfDigitsOdNum(num))