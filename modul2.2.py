first = 6
second = 5
third = 6
result = int(input('введите число'))
if (result == first and result == second and not result == third
        or result == second and result == third and not result == first
        or result == first and result == third and not result == second):
    print(2)
elif result == first and result == third and result == second:
    print(3)
elif not result == first and not result == second and not result == third:
    print(0)