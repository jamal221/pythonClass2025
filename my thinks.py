def maghsoum(n):
    
    #n=int(input("عدد را درج کنيد"))
    list1=list()
    for i in range(n,n*n):
        if n/i==n :
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
    print(bmmA_B)
