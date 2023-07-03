min_limit = 1
max_limit = 100000
while True:
    print('введите положительное число', min_limit, 'and', max_limit)
    num = float(input())
    if num < min_limit or num > max_limit:
        print('введите положительное число от 0 до 100000')
        break
    if num // 1 or num // num:
        print('число является простым')
    else:
        print('число является составным')
    break
