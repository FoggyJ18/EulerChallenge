##############
## Difference of 2 sums
##############


def diff_2_sums(limit):
    sum_of_squared = 0
    squared_sum = 0
    for test in range(1, limit+1):
        sum_of_squared += test * test
        squared_sum += test
    final_answer = (squared_sum * squared_sum) - sum_of_squared
    print('The sum of all squared integers in the given range is ' + str(sum_of_squared) + '.\nThe sum of all the '
          'integers in the given range squared is ' + str(squared_sum*squared_sum) + '.\n The difference of the '
          '2 numbers is ' + str(final_answer) + '.')


diff_2_sums(100)
