# Written by *** and Ruikai Li for COMP9021



import sys
from random import seed, randrange


try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()

I = []
for i in str(x):
    I.append(int(i))
    sum_of_digits_in_x = sum(I)

for n in L:
    n = str(n)
    if n[0] > n[-1]:
        first_digit_greater_than_last += 1
    elif n[0] < n[-1]:
        last_digit_greater_than_first += 1
    elif n[0] == n[-1]:
        same_first_and_last_digits += 1

for number in L:
    for i in [str(number)]:
        distinct_number = len(set(i))
        distinct_digits[distinct_number] += 1

for s in L:
    s = str(s)
    if abs(int(s[0]) - int(s[-1])) < min_gap:
        min_gap = abs(int(s[0]) - int(s[-1]))
    elif abs(int(s[0]) - int(s[-1])) > max_gap:
        max_gap = abs(int(s[0]) - int(s[-1]))

fl_list = []
count_list = []
max_list = []
for m in L:
    m = str(m)
    fl = (int(m[0]), int(m[-1]))
    fl_list.append(fl)
    count_list.append((fl, fl_list.count(fl)))
for q in count_list:
    max_list.append(q[1])
for r in count_list:
    if r[1] == max(max_list):
        first_and_last.add(r[0])


print()
print('x is:', x)
print('L is:', L)
print()
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
     )
print()
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
     )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
     )