#Chap 06. Heapsort
#Page 6-1

def MaxHeapify(A, S, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < S and A[i] < A[l]:
        largest = l
    
    if r < S and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, S, largest)

def BuildMaxHeap(A):
    S = len(A)
    for i in range(S // 2, -1, -1):
        MaxHeapify(A, S, i)

def Heapsort(A):
    S = len(A)

    BuildMaxHeap(A)

    for i in range(S - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        MaxHeapify(A, i, 0)

A = [1, 8, 4, 9, 7, 21, 33, 6, 5, 55, 22, 17, 26, 36, 24, 13, 11]
Heapsort(A)
print(A)

