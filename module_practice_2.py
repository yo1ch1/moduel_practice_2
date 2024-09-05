n = int(input('Введите число от 3 до 20: '))
t = 0
p = 0
ans = []


while True:
    if 3 <= n <= 20:
        print(f'Ваше число: {n}')
        break
    else:
        print('Введено неверное число!')
        break
for i in range(1, 20):
    for j in range(1,20):
        if n % (i+j) == 0:
            if i < j:
                ans.append(i)
                ans.append(j)
        elif n % (i+j) != 0:
            j+=1
        else:
            i+=1


result = (''.join(map(str, ans)))


print(f'Ваш пароль: {result}')