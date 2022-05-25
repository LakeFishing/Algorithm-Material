#Chap 08. Sorting in Linear Time
#Page 8-2

def CountingSort(A):
    k = 34
    B = [0] * len(A)
    C = [0] * k

    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1
    
    A = B
    print(A)

A = [1, 8, 4, 9, 7, 21, 33, 32, 6, 5, 25, 18]
CountingSort(A)

