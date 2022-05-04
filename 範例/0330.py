i = 0
li = []
di = { }

while i < 5:
    li.append(input())
    i += 1


['1', '3', '3', '4', '5', '6', '7', '8', '9', '10']

for j in li:
    if j in di.keys():
        di.update({j : di[j] + 1})
    else:
        di.setdefault(j, 1)

print(di)

# 709
# lambda