#مقسوم عليه هاي يک  عدد


def maghsum():
    k=int(input("عدد را درج نماييد"))
    n=int(input("عدد را درج نماييد"))
    list1=list()
    list2=list()
    for i in range(1,n+1)or(1,k+1):
        if n%i==0 or k%i==0:
            list1.append(i)
            list2.append(i)
            #change varibale one step
    return list1
    return list2
