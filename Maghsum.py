#مقسوم عليه هاي يک  عدد
n=int(input("عدد را درج نماييد"))

for i in range(1,n+1):
    if n%i==0:
        print(i)
