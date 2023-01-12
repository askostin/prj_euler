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

from numtheory import primes, comb
import time

# This array is for only two different groups of digits,
# where all permutations of all digits from each group
# form only prime 4-digits numbers.
# (It's known fact that there are only two such groups).

answer = []

# Build the list of all 4-digits prime numbers.
start_time = time.time()
primes_4d = [x for x in primes.primes(9991) if x > 1000]

def prime_permutations(p_list):
	if not p_list:
		return
	p = p_list[0]
	p_perms = [x for x in comb.digits_permutations(p)
			   if ((x%2!=0) and (x in p_list))]
	if len(p_perms) > 2:
		combs_by_3 = comb.combinations(p_perms, 3)
		for i in range(len(combs_by_3)):
			s = combs_by_3[i]
			if (s[2] - s[1]) == (s[1] - s[0]):
				answer.append(s)
	prime_permutations([x for x in p_list if (x not in p_perms)])

prime_permutations(primes_4d)
print(answer)
print(f"Total time: {round(time.time()-start_time,6)} seconds")
# Total time is 97.5 s
