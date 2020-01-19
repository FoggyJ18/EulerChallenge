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
    print(final_answer)


diff_2_sums(100)
