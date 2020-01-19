###############
## Largest Prime Factor
###############


def lpf_of_int(number_to_check):
    factors = []
    top_of_range = int(number_to_check / 2)
    for number in range(2, top_of_range):
        if number_to_check % number == 0:
            factors.append(number)
    print(factors[-1])


lpf_of_int(600851475143)
