import sys

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

def reverse(s):
    return s[::-1]

def bitcode(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(-(n+1)/2)
    
def codebit(n):
    if n >= 0:
        return 2 * n
    else:
        return 2 * (-n) - 1
    
def display(L):
    print('{', end = '')
    print(', '.join(str(e) for e in L), end = '')
    print('}')

def decode(encoded_set):
    decode_list = []
    reverse_str = reverse(bin(encoded_set))
    for i in range(len(reverse_str)):
        if reverse_str[i] == '1':
            decode_list.append(bitcode(i))
    return sorted(decode_list)
    # REPLACE RETURN [] ABOVE WITH YOUR CODE 
    
def code_derived_set(encoded_set):
    list1 = decode(encoded_set)
    list2 = [] #保存derived code
    bit_list = [] #保存bit number
    x = 0
    for i in list1:
        x += i
        list2.append(x)
    derived_list = sorted(list2)
    for j in derived_list:
        bit_list.append(codebit(j))
    if bit_list == []:
        new_bin_str = '0'
    else:
        bin_str = '0' * (max(bit_list)+1)
        list_bin_str = list(bin_str)
        for k in bit_list:
            list_bin_str[k] = '1'
        new_bin_str = ''
        for m in list_bin_str:
            new_bin_str += m
        new_bin_str = reverse(new_bin_str) #转化为二进制数
    
    return int(new_bin_str, 2)
    # REPLACE RETURN 0 ABOVE WITH YOUR CODE 

print('The encoded set is: ', end = '')
display(decode(encoded_set))
code_of_derived_set = code_derived_set(encoded_set)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end = '')
display(decode(code_of_derived_set))
