# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
n3 = 1
n5 = 1
for i in range(1, 1000) :
    if n3 == 3 :
        n3 = 1
    else :
        n3 = n3 + 1

    if n5 == 5 :
        n5 = 1
    else:
        n5 = n5 + 1
        
    if  (n3 == 1 or n5 == 1)  :
        sum = sum + i

print(sum)

# answer is 233168