def Judge(num):
    if num == 0:
       return 0
    if num == 1:
       return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 0
    return 1

number = 1051043

for a in range(1, number):
    if Judge(a) == 1 and (a + number) % 3 == 0:
        print(a)
        break