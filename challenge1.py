##################
## sum of multiples of 3 & 5 between 1 & 1000
##################

sum = 0

for number in range(1, 1001):
    if number % 3 == 0 or number % 5 == 0:
        sum += number

print('The sum of all numbers divisible by 3 or 5, range 1-1000, is {}.'.format(sum))
