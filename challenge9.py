###############
## Special Pythagorean Triplet
###############


def find_triplet(max_of_range):
    for int_a in range(1, max_of_range):
        for int_b in range(1, max_of_range):
            if int_a + int_b < max_of_range:
                int_c = max_of_range - int_a - int_b
                a_squ = int_a * int_a
                b_squ = int_b * int_b
                c_squ = int_c * int_c
                if a_squ + b_squ == c_squ:
                    return '{}, {} and {} are the Special Pythagorean Triplets'.format(int_a, int_b, int_c)
    return '{} does not have any Pythagorean Triplets'.format(max_of_range)


print(find_triplet(1000))
