def gcd(a, b):
    # محاسبه ب.م.م با الگوریتم اقلیدس
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # محاسبه ک.م.م با استفاده از ب.م.م
    return abs(a * b) // gcd(a, b)

# مثال
num1 = int(input("عدد اول را وارد کنید: "))
num2 = int(input("عدد دوم را وارد کنید: "))

result = lcm(num1, num2)
print(f"ک.م.م {num1} و {num2} برابر است با: {result}")
