# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import NumTheory.dividers

lst = [[3,1],[2,1]]
n = 1

for d in range(4,21,1) :
	dvs = NumTheory.dividers.dividers2(d)
	print(dvs,'is checked:')
	for pair in dvs :
		# поиск в @lst пары @pair_lst=[@d1, @p1], где первый элемент равен первому элементу @pair=[@d, @p]
		is_in_list = [x for x in lst if (x[0] == pair[0])]
		if (is_in_list) :
		# если существует @pair_lst, то если @p1>@p, то установить @p = @p1
			pair_lst = is_in_list[0]
			print(pair, ' is compared to ', pair_lst, ' from the list')
			if (pair[1] > pair_lst[1]) :
				index = lst.index(pair_lst)
				lst[index] = [pair_lst[0], pair[1]]
		# если не найдена @pair1, то добавить @pair в @list
		else :
			lst = [pair] + lst

		print(lst)
		print('******')

for p in lst :
	n *= p[0]**p[1]

print (n)

# answer is 232792560
