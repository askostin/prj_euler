# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# ...

# 3-digit number lies in range [100..999], so the product of two such numbers lies in range [10000..998001].
# There are two types of palindromes -- 5- and 6-digits.
# The first ones are in the range [10001..99999], the second ones -- in the range [100001..997799]
# We should begin with the second one.

# a*10^5 + b*10^4 + c*10^3 + c*10^2 + b*10 + a = a*(10^5 + 1) + b*10(10^3 + 1) + c*10^2*(10+1)
# a = 1..9, b = 0..9, c = 0..9

import numtheory

# find_pldr : void -> N
def find_pldr() :
	flag = False
	comb = []
	comb_temp = []
	n = 0
	n_temp = 0
	dvs = []
	dvs_temp = []
	# Look through all palindroms d = {abccba}, a = 9..1, b = 9..0, c = 9..0
	for a in range(9,0,-1) :
		n1 = a*100001
		for b in range (9,-1,-1) :
			n2 = b*10010
			for c in range(9,-1,-1) :
				n = n1 + n2 + c*1100
				if (n <= 998001) :
					# Create the list of all dividers of the given number
					dvs = numtheory.dividers2(n)
					dvs.reverse()
					if ((len(dvs) > 1) or ((len(dvs) == 1) and ((dvs[0])[1] > 1))) :
						comb = check_product(n, dvs, 1)
						if (comb and (n > n_temp)) : # (comb != None) and (comb != [])
							n_temp = n
							dvs_temp = dvs
							comb_temp = comb
							flag = True
	if (flag) :
		print(n_temp, ' = ', comb_temp[0], ' * ', comb_temp[1])
		return True
	else :
		return False

# check_product : N listof(list(N, N)) N -> list(N, N) -or FALSE
# check_product(n, lst, n1)
# Finds the combination of numbers @group, when two products of numbers from two groups from the list are 3-digit numbers: 100 <= n1*group, n/(n1*group) <= 999
def check_product(n, lst, n1) :
	# If all dividers depleted, and no suitable combinations was found (otherwise the solution would have been returned).
	if (lst == []) :
		return []
	else :
		# Take the first divider @d1, which is maximum (list of dividers is reversed).
		# @d1 is in the list [@d1, @p1], where @p1 is the max power, when @d1**@p1 is still a divider of n.
		d1 = (lst[0])[0]
		## Делитель больше 1000 и решать задачу смысла нет, т.к. для любой комбинации двух произведений делителей одно из произведений будет иметь больше чем 3 знака:
		if (d1 > 999) :
			return []

		p1 = (lst[0])[1]
		n1_temp = n1 * d1

		## Добавление элементарного делителя @d1 оказалось неудачным, сразу переходим к следующему делителю @d2
		if (n1_temp > 999) :
			return check_product(n, lst[1:], n1)

		## Делитель трёхзначный и число n/n1 тоже трёхзначное, то мы решили задачу:
		if ((100 <= n1_temp) and (100 <= n/n1_temp <= 999)) :
			return  [n1_temp, n/n1_temp]

		## Делитель меньше 100 и остались ещё делители.
		### (a) Делитель @d1 в списке оставшихся делителей @lst был в степени 1, переходим к делителю @d2.
		if (p1 == 1) :
			lst = lst[1:]
		### (б) Делитель d1 в списке оставшихся делителей @lst был в составе произведения вида @d1*@d1*... (@p1 > 1), и мы пробуем его добавить ещё раз
		else :
			lst = [[d1, p1 - 1]] + lst[1:]

		solution = check_product(n, lst, n1_temp)
		### Или для (а), или для (б) мы нашли решение, @d входит в составной 3-значный делитель.
		if ((solution != []) and (solution != None)) :
			return solution
		### Не получилось найти решение, когда мы: или добавили единственный оставшийся делитель @d1 в комбинацию, или на следующем шаге добавили в комбинацию ещё один оставшийся делитель @d1.
		### (в) @p1 >= 1, но добавление делителя в комбинацию оказалось неудачным, убираем его из комбинации и переходим к следующему.
		else :
			return check_product(n, lst[1:], n1)

find_pldr()

#answer is 906609
