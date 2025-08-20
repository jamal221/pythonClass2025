#Kmm class
def maghsoum(n):
    
    #n=int(input("عدد را درج کنيد"))
    list1=list()
    for i in range(1,n+1):
        if n%i==0:
            list1.append(i)
    return list1

def bmm(a,b):
    maghsumA=maghsoum(a)
    maghsumB=maghsoum(b)

    #make set from list
    setA=set(maghsumA)
    setB=set(maghsumB)

    #Intersect two sets
    commonA_B=setB.intersection(setA)
    commonA_B_list=list(commonA_B)
    bmmA_B=max(commonA_B_list)
    return bmmA_B

def kmm(a,b):
    return (a*b)/bmm(a,b)

def kasr():
    souart1=int(input("صورت 1 را وارد نماييد"))
    souart2=int(input("صورت2 را وارد نماييد"))
    makh1=int(input("مخرج 1 وارد نماييد"))
    makh2=int(input("مخرج 2 را وارد نماييد"))

    #kmm makh1 and makh2
    print(bmm(makh1,makh2))
    kmmAB=kmm(makh1,makh2)

    # souraAll1
    souratAll1=(kmmAB/makh1)*souart1

    #souratAll2
    souratAll2=(kmmAB/makh2)*souart2
    #souratAll
    souratAll=souratAll1+souratAll2
    #print result
    print(str(souratAll)+"/"+str(kmmAB))
