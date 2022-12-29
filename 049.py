# Prime permutations

# The arithmetic sequence, 1487, 4817, 8147, in which each of
# the terms increases by 3330, is unusual in two ways:
# 1) each of the three terms are prime,
# 2) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-,
# or 3-digit primes, exhibiting this property, but there is
# one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating
# the three terms in this sequence?

from numtheory import primes, dividers

# This array is for only two different groups of digits,
# where all permutations of all digits from each group
# form only prime 4-digits numbers.
# (It's known fact that there are only two such groups).

answer = [[0]*3]*2

# Counter of the solutions registered in @answer.

n = 0

# Temporary array, where all the permutations of the digits
# from the number are placed

temp = []

# Step 1: Build the list of all 4-digits prime numbers.

all_primes = [x for x in primes.primes_list(9991) if x > 1000]

# Step 2: Sequentally take prime numbers from list and check set of digits
# of each number if there are at least two prime numbers, formed by permutations
# of these digits (and they have to be in the list of primes):
# - if "yes" -- write list of these permutations in @array;
# - if "no", remove from @all_primes the number itself and, if exists,
# the only premutations of its digits, forming prime number.

def prime_permutations(p_list):
    if p_list:
        temp = [x for x in p_list if ((x%2 != 0) and (not (x in p_list)))]
        if len(temp) > 2:
            for i in (0, 3):
                answer[n][i] = temp[i]
            n += 1
            if n == 2:
                return answer
        else:
            # remove all elements of @temp from the p_list
            for i in temp:
                p_list.remove(i)
            prime_permutations(p_list)
    else:
        return answer

#print(prime_permutations(all_primes))
