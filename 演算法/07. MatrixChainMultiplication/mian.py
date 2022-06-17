#Chap 15. Dynamic Programming
#Page 15-5

import sys
def MatrixChainOrder(p):
    n = len(p)
    m = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]
    for i in range(1, n):
        m[i][i] = 0
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    for item in s[1:]:
        print('\n')
        for value in item[1:]:
            print("%-6s" %(value), end = '')
    print('\n')
    
    for item in m[1:]:
        print('\n')
        for value in item[1:]:
            print("%-6s" %(value), end = '')
    print('\n')
    return m[1][n - 1]

p = [30, 50, 20, 100, 5, 40, 80, 10, 50, 20, 100]
print(str(MatrixChainOrder(p)))
