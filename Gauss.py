import math

n = int(input("Nhập vào số ẩn: "))

a = [[2, -1, 1, 4],
    [3, 2, -2, -1],
    [1, 3, -1, 3]]

def Gauss(a, n):
    for i in n:
        for j in n:
            if a[i][j] == 0 and i == j:
                l = i+1
                
                if a[l][i] == 0:
                    l+=1
    pass




if __name__ == '__main__':
    pass
    