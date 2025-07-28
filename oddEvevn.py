#School: Odd and even
def checkEvenOdd():
    num=int(input("عدد را وارد نماييد"))
    if(num>0 and  num%2==0):
        print("عدد زوج است")
    elif(num>0 and num%2!=0):
        print("عدد فرد است")
    else:
        print("عدد شما در محدوده ي برنامه نيست")
