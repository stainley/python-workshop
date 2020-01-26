x = 24
y = 36
i = 1
counting = True
while counting:

    if i % x == 0 and i % y == 0:
        print('The Least Common Multiple of ', x, ' and ', y, ' is', i, '.')
        break
    i += 1
