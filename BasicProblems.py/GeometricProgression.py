
def geomatricPro(a,r,n):
    sum = 0
    i = 0

    while(i < n):
        sum = sum + a
        a = a * r
        i += 1 

    return sum

 
if __name__ == '__main__':
    a = 1
    r = 0.5
    n = 10
    print(geomatricPro(a,r,n))