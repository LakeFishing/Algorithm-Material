# 901
a = 5
while a > 0:
    b = input('write')
    f = open('write.txt', 'a')
    f.write(b)
    f.close()
    a -= 1

# 906
f_name = input()
str_old = input()
str_new = input()

f = open(f_name, 'r+')
data = f.read()

print('old')
print(data)

datas = data.replace(str_old, str_new)
print('new')
print(datas)

f.write(datas)
f.close()
