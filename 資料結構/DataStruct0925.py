m,n,o=map(int,input().split()) #輸入矩陣大小 m * n , n * o

#創立矩陣
A = [[0]*n for _ in range(m)]  
B = [[0]*o for _ in range(n)]
C = [[0]*o for _ in range(m)]


#逐列輸入矩陣 A
for i in range(m):
    A[i]=list(map(int,input().split()))

#印出矩陣 A 內容
print(A)

#逐列輸入矩陣 B
for i in range(n):
    B[i]=list(map(int,input().split()))

#印出矩陣 B 內容
print(B)

#矩陣 A X B 的運算結果存入矩陣 C
for i in range(m):
    for j in range(o):
        for k in range(n):
            C[i][j]+=A[i][k]*B[k][j]
    
#印出矩陣 C
print(C)