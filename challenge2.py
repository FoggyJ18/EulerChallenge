##############
## Even Fibonacci Numbers
##############

sum = 2

term1 = 1
term2 = 2
new_term = term1 + term2

while new_term <= 4000000:
    new_term = term1 + term2
    if new_term % 2 == 0:
        sum += new_term
    term1 = term2
    term2 = new_term
