year = int(input('enter year yyyy: '))
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print('regular')
else:
    print('leap')
