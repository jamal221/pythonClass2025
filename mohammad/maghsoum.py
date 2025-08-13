# maghsoum
def maghsoum(n):
    
    #n=int(input("عدد را درج کنيد"))
    list1=list()
    for i in range(1,n+1):
        if n%i==0:
            list1.append(i)
    return len(list1)
# aadade aval o morakab
def awal(n):
    if maghsoum(n)==2:
        print("عدد اول است")
    else:
        print("عدد مرکب است")
#shomaresh aadade awal
def shomaresh(n):
    list2=list()
    for i in range(1,n+1):
        if maghsoum(i)== 2:
            list2.append(i)
    return len(list2)
