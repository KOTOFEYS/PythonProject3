result = (int(input('Введите число ')))
for i in range(1, 20):
    if i == result/2:
        break
    for j in range(1, 20):
        if j == 1:
            continue
        if (result % (i + j)) == 0:
            print(i, end = ' ')
            print(j, end = ' ')
        if j == result:
         break







