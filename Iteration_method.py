#iteration_method
import math
from tabulate import tabulate

print("Tìm nghiệm của phương trình x**3+x-1000 trên khoảng phân ly: ", end = '')
a, b = map(int, input().split())
print("Nhap vao ham \u03C6 (x): math.pow(12x+5, 1/3)") # \u03C6 là ký hiệu toán học
error = float(input("Nhập vào sai số: "))

def phi(x):
    return math.pow(1000-x, 1/3)

X_n = [[0, 10]]

def test(a, b):
    x_1= phi(b)
    i = 1
    while abs(x_1-b) > error:
        ls = [i, x_1]
        X_n.append(ls)
        b = x_1
        x_1 = phi(b)
        i +=1
    
    col_names = ["n", "X_n"]
  
    print("Kết quả được ghi trong bảng sau: ")
    print(tabulate(X_n, headers=col_names, tablefmt="fancy_grid"))
    
test(a, b)

