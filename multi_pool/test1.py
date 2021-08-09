# 打印出100以内所有十位数比个位数大1位的数字。

for i in range(0,10):
    for j in range(0,10):
        if i == j+1:
            print(i*10+j)

li = [i*10+j for i in range(0,10) for j in range(0,10) if i == j+1]
print(li)

res = lambda a : a*a
print(res(6))

letter = ['w','z','y']
for i,v in enumerate(letter):
    print(i,v)
    