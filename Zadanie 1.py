zna41 = input ('Введите значения для первого массива, с пробелами между значениями: ').split()
zna41_list = list(zna41)
print("Введенный массив:", zna41_list)

zna42 = input ('Введите значения для второго массива, с пробелами между значениями: ').split()
zna42_list = list(zna42)
print("Введенный массив:", zna42_list)

chislo = input ('Введите позицию, начиная с которой будет производиться запись в первый массив, всех значения второго: ')
chislo = int(chislo)

l1 = zna41_list[:chislo]
for i in range(len(zna42_list)):
    l1.append(zna42_list[i])
for i in range(chislo+1,len(zna41_list)):
    l1.append(zna41_list[i])
print(l1)