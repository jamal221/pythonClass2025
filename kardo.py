#magsum
def mghsum(n):
    list1=[]
    for i in range(1,n+1):
        if n%i==0:
            list1.append(i)
    return len (list1)
    # تعداد مقسوم عليه ها را بر مي گرداند
#compaere
def compaere (n):
    if mghsum(n)==2:
        return 1
    else:
        return 0

def checkPrimeAll():
    digit=int(input("رنج دلخواه را درج نماييد"))
    listPrime=[]
    for i in range(2, digit+1):
        if compaere(i)==1:
            listPrime.append(i)
    print("تعداد اعداد اول برابر است با",len(listPrime))
    print("اعداد اول در اين محدوده برابر است با:   ",listPrime)
