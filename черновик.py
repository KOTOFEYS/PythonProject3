result = (int(input('Введите число ')))
i = 1
while i <= 20:
  if i == result / 2:
    break
  j = 2
  while j <= result:
    if (result % (i + j)) == 0:
      print(i, end = ' ')
      print(j, end = ' ')
    j = j + 1
  i = i + 1


