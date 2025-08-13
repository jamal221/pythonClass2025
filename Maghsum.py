#مقسوم عليه هاي يک  عدد
def magsum(n):
    #n=int(input("عدد را درج نماييد"))
    list1=list()
    for i in range(1,n+1):
        if n%i==0:
            list1.append(i)
    return len(list1)
def mor(n):
    if magsum(n)== 2:
        print("عدد اول است")
    else:
        print("عدد مرکب است")
        
