playground = [[None, None, None],
              [None, None, None],
              [None, None, None]]
i = 1
last_value = ''
while i <= 3:

    value = ''
    if i % 2 == 0:
        print('ход x')
        value = 'x'
    else:
        print('ход o')
        value = 'o'

    position_r = int(input('введите строку')) - 1
    position_c = int(input('ведите столбец')) - 1
    if playground[position_r][position_c] is None:
        playground[position_r][position_c] = value
    else:
        print('нельзя так делать')

    print('\n' * 30)
    print('   ', 1, '   ', 2, '   ', 3)
    print(" 1", playground[0], '\n', 2, playground[1], '\n', 3, playground[2], '\n', )

    last_value = value
    i += 1
