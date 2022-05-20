#Chap 02. Getting Started
#Page 1-5

import math

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    
    L = [None] * (n1 + 1)
    R = [None] * (n2 + 1)
    
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]

    L[n1] = math.inf
    R[n2] = math.inf

    i = 0
    j = 0
    k = p

    for m in range(k, r + 1):
        if L[i] <= R[j]:
            A[m] = L[i]
            i += 1
        else:
            A[m] = R[j]
            j += 1

def mergeSort(A, p, r):
    if p < r:
        q = int((p + r) // 2)
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)

count = int(input('共幾個數字？'))
quizList = []
for i in range(count):
    quizList.append(int(input('第 %d 個數字：' %(i + 1))))

print('0', quizList, 0, count - 1)
mergeSort(quizList, 0, count - 1)
print('結果：%s' %(quizList))
