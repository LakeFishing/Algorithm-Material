#Chap 15. Dynamic Programming
#Page 15-1

def PrintStations(l, n, L):
    i = l
    print('Line %s, station %s' %(i, n))
    for j in range(n, 1, -1):
        i = L[i - 1][j - 2]
        print('Line %s, station %s' %(i, j - 1))

def FastestWay(a, t, e, x, n):
    F1 = [None] * n
    F2 = [None] * n
    L = [[None] * (n - 1), [None] * (n - 1)]

    F1[0] = e[0] + a[0][0]
    F2[0] = e[1] + a[1][0]

    for j in range(1, n):
        if F1[j - 1] + a[0][j] <= F2[j - 1] + t[1][j - 1] + a[0][j]:
            F1[j] = F1[j - 1] + a[0][j]
            L[0][j - 1] = 1
        else:
            F1[j] = F2[j - 1] + t[1][j - 1] + a[0][j]
            L[0][j - 1] = 2
        if F2[j - 1] + a[1][j] <= F1[j - 1] + t[0][j - 1] + a[1][j]:
            F2[j] = F2[j - 1] + a[1][j]
            L[1][j - 1] = 2
        else:
            F2[j] = F1[j - 1] + t[0][j - 1] + a[1][j]
            L[1][j - 1] = 1
    if F1[n - 1] + x[0] <= F2[n - 1] + x[1]:
        print(F1)
        print(F2)
        print('總用時 = %s, 終點 = %s' %(F1[n - 1] + x[0], 1))
        PrintStations(1, 6, L)
    else:
        print('總用時 = %s, 終點 = %s' %(F2[n - 1] + x[0], 2))
        PrintStations(2, 6, L)

a = [[7, 9, 3, 4, 8, 4], [8, 5, 6, 4, 5, 7]]
t = [[2, 3, 1, 3, 4], [2, 1, 2, 2, 1]]
e = [2, 4]
x = [3, 2]
n = 6
FastestWay(a, t, e, x, n)
