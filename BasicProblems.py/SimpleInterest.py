def SimpleInterest(p,r,t):
    rate_Per_month = p * (r / 100)
    tot = int(rate_Per_month * t)

    return tot
     
if __name__ == '__main__':
    p = 3000
    r = 7
    t = 1
    print(SimpleInterest(p,r,t))