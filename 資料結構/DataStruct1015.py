import numpy as np #引入 numpy 套件

m,n,o=map(int,input().split()) #輸入矩陣大小 m * n , n * o

#創立矩陣
A = [[0]*n for _ in range(m)]  
B = [[0]*o for _ in range(n)]


#逐列輸入矩陣 A
for i in range(m):
    A[i]=list(map(int,input().split()))

#將串列 A 轉成 ndarray
A=np.asarray(A)

#印出矩陣 A 內容
print(A)

#逐列輸入矩陣 B
for i in range(n):
    B[i]=list(map(int,input().split()))

#將串列 B 轉成 ndarray
B=np.asarray(B)

#印出矩陣 B 內容
print(B)

#印出矩陣 A X B 的內容
print(np.dot(A,B))