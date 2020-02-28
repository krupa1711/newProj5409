import random
import time
import datetime
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


f = open("random_number.txt", "r")
list1=f.readlines()
print(list1)

for i in list1:
    N=i
    start_time = time.time() * 1000
    result = factorial(int(i))
    end_time = time.time() * 1000
    requestID = random.randint(1,10)
    time_taken = (end_time-start_time)
    print("RequestID : ", requestID ,"Time : ",time_taken,"result : ",result,"N :",N)


