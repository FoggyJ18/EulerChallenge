#############
## Smallest Multiple
#############


def smallest_multiple(high_limit):
    tested_int = high_limit
    multiple_found = False
    while not multiple_found:
        step = high_limit - 1
        while step > 1:
            if tested_int % step != 0:
                step = 1
                tested_int += high_limit
            elif step == 2:
                step -= 1
                multiple_found = True
            else:
                step -= 1
    print(str(tested_int) + ' is the smallest multiple of all numbers in range 1-' + str(high_limit))


smallest_multiple(20)
