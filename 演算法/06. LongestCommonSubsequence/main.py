#Chap 15. Dynamic Programming
#Page 15-16

def LCSLength(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for x in range(n + 1)] for x in range(m + 1)]
    b = [['' for x in range(n + 1)] for x in range(m + 1)]
    for i in range(1, m + 1):
        c[i][0] = 0
    for j in range(0, n + 1):
        c[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '↖'
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = '↑'
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = '←'
    return c, b

def PrintLCS(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == '↖':
        PrintLCS(b, X, i - 1, j - 1)
        # print(X[i - 1])
        ans.append(X[i - 1])
    elif b[i][j] == '↑':
        PrintLCS(b, X, i - 1, j)
    else:
        PrintLCS(b, X, i, j - 1)

X = ['A', 'B', 'C', 'A', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'D', 'A']
ans = []

c, b = LCSLength(X, Y)
PrintLCS(b, X, len(X), len(Y))

print('\n最長共同部分子序列： ', end='')
for i in range(len(ans)):
    print(ans[i], end='')
for i in range(len(c)):
    for j in range(len(c[i])):
        print('%-5s' %(b[i][j]), end='')
    print('\n')
    for j in range(len(c[i])):
        print('%-5s' %(c[i][j]), end='')
    print('\n')
