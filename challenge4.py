#############
## Largest Palindrome Product
#############


def lpp_of_3dig_int():
    int1 = 100
    int2 = 100
    lpp_factor1 = 101
    lpp_factor2 = 101
    lpp = 0
    while int1 < 1000:
        while int2 < 1000:
            ol_boy = int1*int2
            if str(ol_boy) == str(int1*int2)[::-1]:
                if ol_boy > lpp:
                    lpp_factor1 = int1
                    lpp_factor2 = int2
                    lpp = ol_boy
            int2 += 1
        int2 = 100
        int1 += 1
    print(str(lpp) + ' is the lpp for all 3 digit integers. '
                     'This was the product of ' + str(lpp_factor1) + ' and ' + str(lpp_factor2))


lpp_of_3dig_int()
