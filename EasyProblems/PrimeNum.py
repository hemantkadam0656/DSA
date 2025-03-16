def PrimeNum(n):
    if n == 0 or n == 1:
        return False
    
    for i in range(2,n):
        if n % i == 0:            
            return False 

    return True


if __name__ == '__main__':
    n = 7
    print(PrimeNum(n))