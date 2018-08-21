# Written by *** and Ruikai Li for COMP9021



import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = None
simplest_fractions = []
size_of_most_complex_fraction = None
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []

def divprime(num):
    q = []
    while num != 1:
        for i in range(2, int(num+1)):
            if num % i == 0:
                q.append(i)
                num = num/i
                break
    return q
            


F = []
fractions_list = []
length_list = []
for x in L:
    for y in L:
        if x < y:
            F.append((int(x/gcd(x,y)), int(y/gcd(x,y))))
        else:
            F.append((int(y/gcd(x,y)), int(x/gcd(x,y))))
fractions = set(F)
for i in fractions:
    fractions_list.append(i)

for (x, y) in fractions_list:
    length_list.append(len(str(x))+len(str(y)))
size_of_simplest_fraction = min(length_list)
size_of_most_complex_fraction = max(length_list)
for l in range(len(length_list)):
    if length_list[l] == min(length_list):
        simplest_fractions.append(fractions_list[l])
    if length_list[l] == max(length_list):
        most_complex_fractions.append(fractions_list[l])
simplest_fractions = sorted(simplest_fractions, key=lambda x: x[0]/x[1])
most_complex_fractions = sorted(most_complex_fractions, key=lambda x: x[0]/x[1], reverse=True)




p = []
prime_list = []
for (a, b) in most_complex_fractions:
    p.append(b)
pl = set(p)
for i in pl:
    prime_list.append(i)

count_list = []
cl = []
d_list = []
c_list = []
for m in prime_list:
    div_list = divprime(m)
    for l in range(len(div_list)):
        cl.append((div_list[l], div_list.count(div_list[l])))
for r in set(cl):
    count_list.append(r)

for (c, d) in count_list:
    d_list.append(d)
    c_list.append(c)
for e in range(len(d_list)):
    if d_list[e] == max(d_list):
        largest_prime_factors.append(c_list[e])
largest_prime_factors = sorted(largest_prime_factors)
if d_list == []:
    multiplicity_of_largest_prime_factor = 0
else:
    multiplicity_of_largest_prime_factor = max(d_list)# REPLACE THIS COMMENT WITH YOUR CODE


print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
     )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
     )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
     )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)
        
        
