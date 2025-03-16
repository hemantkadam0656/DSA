lst = [1,2,3,4,5,6,7,8,9,10,11,12]

def even(num):
    if num%2==0:
        return True
    
print(list(filter(even, lst)))
