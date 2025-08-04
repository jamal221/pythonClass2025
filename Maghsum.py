#مقسوم عليه هاي يک  عدد
def maghsum():
    n=int(input("عدد را درج نماييد"))
    list1=list()
    # define variable
    for i in range(1,n+1):
        if n%i==0:
            list1.append(i)
            #change varibale one step
    return list1
