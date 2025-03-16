import threading
import time

def fun(second):
    t1 =  time.time()
    print(f'spleeping time of code is {second}')
    t2 = time.time()
    print(t2- t1)


f1 = threading.Thread(target=fun, args=['Hemant','karan'])
f2 = threading.Thread(target=fun, args=[3])
f3 = threading.Thread(target=fun, args=[1])


f1.start()
f2.start()
f3.start()

# f1 = fun('Hemant')
# f2 = fun('karan')
# f3 = fun('ashish')
