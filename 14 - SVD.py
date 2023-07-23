#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from scipy.linalg import null_space
from numpy import linalg as LA
from scipy.linalg import svd
import math as mt




data=np.genfromtxt('input.txt', delimiter=' ')
A=np.array(data)

m=len(A)
n=len(A[0])

def SVD(A):
# gán ma trân sigma bằng ma trận 0 cở m.n
    sigma = np.zeros((m,n))
    v = np.eye(n)
#    r = rank ma trận -1
    r= np.linalg.matrix_rank(A) -1
# nếu A ko full rank thì sẽ tìm ker(A) và ker(A.T)    
    if r != n-1:
        ns = null_space(A)
        ns =ns.T
        nd = null_space(A.T)
        nd = nd.T
# m >=n ta tính U trước V sau        
    if m>=n:   
        # ta tìm trị riêng w của A.AT và tìm vecto riêng tương ứng là u
        w,u = LA.eig(A@A.T)
        # sắp xếp trị riêng và vetor riêng
        for i in range(n-1):
            for j in range(i+1, n):
                if(w[j-1] < w[j]):
                    w[j], w[j-1] = w[j-1], w[j]
                    u[:,[j-1,j]] = u[:,[j,j-1]]
        U = u.T
    # ta tìm r vector riêng đầu tiên ứng với U
        V= np.zeros((r+1,n))
        for i in range(r+1):
            V[i,:n]=(U[i,:m]@A)/(np.sqrt(w[i]))
        np.fill_diagonal(sigma, np.sqrt(w))
    #sau đó tìm  n - r vector còn lại
        if r != n-1:
            V = np.concatenate((V,ns), axis =0)


# m <n ta tính V trước U sau tương tự
    else:
        w,v = LA.eig(A.T@A)
        for i in range(n-1):
            for j in range(i+1, m):
                if(w[j-1] < w[j]):
                    w[j], w[j-1] = w[j-1], w[j]
                    v[:,[j-1,j]] = v[:,[j,j-1]]
    #    V =v
        U = np.zeros((r+1,m))
        for i in range(r+1):
            U[i,:m]=(v.T[i,:n]@A.T)/(np.sqrt(w[i]))
        np.fill_diagonal(sigma, np.sqrt(w))

        if r != n-1:
            U = np.concatenate((U,nd), axis = 0)

        V = v.T

    return U.T, sigma, V
        

U,sigma,VT=SVD(A)
print("A=")
print(A)
print("U = ")
print(U)
print("S = ")
print(sigma)
print("VT = ")
print(VT)
print("test")
print(A- U@sigma@VT)
print("---------------------------------")
print('Using scipy')
U,S,VT = svd(A)
S=np.diag(S)
print("U=")
print(U)
print("S=")
print(S)
print("VT=")
print(VT)


# In[ ]:





# In[ ]:




