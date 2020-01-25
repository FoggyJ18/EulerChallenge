############
## 10001st Prime #
############
import math

def find_a_prime(which_prime):
    prime_counter = 6
    # the question gives that 13 was already tested and it's a known that all evens are not primes, so we start w/ 15
    tested_int = 15
    prime = 13
    prime_dictionary = {1: 2, 2: 3, 3: 5, 4: 7, 5: 11, 6: 13}
    if prime_counter >= which_prime:
        print("{} is the prime you are looking for.".format(prime_dictionary[which_prime]))
    else:
        dividend = math.floor(tested_int / 2) - 1
        while prime_counter < which_prime:
            if tested_int % dividend == 0:
                tested_int += 2
                dividend = tested_int - 1
            elif tested_int % dividend != 0 and dividend == 3:
                prime = tested_int
                prime_counter += 1
                tested_int += 2
                dividend = math.floor(tested_int / 2) - 1
            else:
                dividend -= 1
        print("{} is the prime you are looking for.".format(prime))


find_a_prime(1000)
# 104743
