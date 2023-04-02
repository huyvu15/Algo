# bisection method

import math

print("Tìm nghiệm của hàm số f(x) = x^x -10 trên khoảng: ")
# (a, b)
print("Nhap vao khoang (a, b): ", end = "")
a, b = map(int, input().split())

# enter error value

error = float(input("Nhap vao sai so: "))

n = float(math.ceil(math.log((b-a)*(error**(-1)), 2)))

print("số lần lặp là: ", int(n))

def f(x):
    return x**x-10

def test(a, b):
    i = 1
    while abs(b - a) >= error:
        c = (a+b)/2
        if f(a)*f(c) < 0:
            print(f"lần {i}: a = {a}, b = {b}, c = {c}, f(c) = ", f(c))
            b = c
        else:
            print(f"lần {i}: a = {a}, b = {b}, c = {c}, f(c) = ", f(c))
            a = c
        i +=1
    return c   
print("Cách thuật toán chạy:")
print("Nghiệm của phương trình là: ",test(a, b))



