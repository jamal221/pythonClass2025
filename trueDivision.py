def maghsum(num):
    
    divisors =[]
    
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
          
    return len(divisors)

#  عدد بررسي جهت اول بودن
def primeNumber(n):
    if maghsum(n)==2:
        print("عدد اول است")
    else:
        print("عدد مرکب است")
