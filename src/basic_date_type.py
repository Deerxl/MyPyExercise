"""
this is a kind of notes
"""
from random import Random # from package random import Random func

# print
print("Hello, Xiaolu!", "This is the first day learning Python")

# get random number / if-else
random = Random()
rand_int = random.randint(1, 100)
if rand_int % 3 == 0:
    print("mod 3 == 0:", rand_int)
elif rand_int % 3 == 1:
    print("mod 3 == 1:", rand_int)
else:
    print("mod 3 == 2", rand_int)

#string examples
str1 = "12345678"
print("str.len", len(str1))
print("str[0: 5]", str1[0: 5])
print("str[0: -1]", str1[0: -1]) # -1 represents the last index of the str
print("str[0: -3]", str1[0: -3]) # -3 represents the third index of the str from the right
print("str[0: 10]", str1[0: 10])
print("str[0: 9]", str1[0: len(str1) + 1])
print("str[3:]", str1[3:])
print("str[:3]", str1[:3])
print("str*2", str1 * 2)

print('he\nllo')
print(r'he\nllo') # 'r' means '\' doesn't effect

# types of data
name = "xiaolu"
age = 18
weight = 48.50
lily_weight = wendy_weight = weight
print(name, age, weight, lily_weight, wendy_weight)

school, grade, classname = "whu", 2, "class-1"
print(school, grade, classname)

# numbers
a, b, c, d = 1, 4.5, True, 1+2j
print(type(a), type(b), type(c), type(d))

# instance
print(isinstance(a, int), isinstance(b, int), isinstance(c, int), isinstance(d, int))

# bool
print("True + 1: ", True + 1)
print("False - 1: ", False - 1)

# del obj
del a, b, c, d

# operation
a, b, c, d = 1, 2, 3, 3.1
print('a / c: ', a / c) # '/' return float
print("a // c: ", a // c) # '//' return integer
print('2**3: ', 2**3) # '**' pow

if (n := len(str1)) > 5: # ':=' assign and return
    print(f"len > 5: {n} > 5: {str1}")

# list
my_list = [1, 2, 'a', 3.5, True, 3]
print(my_list)
my_list[0] = 'xiaolu'
print(my_list)
my_list[2:4] = []
print(my_list)
print(my_list * 2)

# func define / list / str
def reverse_words(input_str):
    input_words = input_str.split(" ")
    input_words = input_words[::-1]
    output = " ".join(input_words)
    return output

# tuple: just like list
tup1 = (1, 2, 3.14, True)
# tup1[2] = [] tuple cannot be modified
tup2 = (2, )
print(tup2)

# set
my_set = set(tup1)
print(my_set)

sites_set = {'Google', 'Facebook', 'Alibaba', 'ByteDance'}
if 'Google' in sites_set:
    print("Google found")
else:
    print("Google not found")

set_a = set('abccccd')
set_b = set('abdddde')
print('set_a', set_a)
print('set_b', set_b)
print('set_a & set_b', set_a & set_b)
print('set_a - set_b', set_a - set_b)
print('set_a | set_b', set_a | set_b)
print('set_a ^ set_b', set_a ^ set_b)


# dictionary (key, value)
my_dict = {'a': 1, 2: 'b'}
print('my_dict', my_dict)
print('my_dict.get(\'a\')', my_dict.get('a'))
print('my_dict.keys()', my_dict.keys())

my_dict2 = dict([('a', '1'), ('b', '2'), ('c', '3')])
print('my_dict2', my_dict2)

my_dict3 = {x : x**2  for x in [1, 2, 3]}
print('my_dict3', my_dict3)

# bytes
bytes_a = b"hello"
bytes_b = bytes_a[1:-1]
bytes_c = bytes_a + b"world"
print(bytes_a, bytes_b, bytes_c)
if bytes_a[0] == ord('h'):
    print("the first character is 'h'")

# type convert
int_num = int("3")
int_num2 = int(3.14)
float_num = float("3")
float_num2 = float(3)
str_convert = str(1.0)
print(int_num, int_num2, float_num, float_num2, str_convert)

if __name__ == "__main__":
    input = 'I like xiaolu'
    rw = reverse_words(input)
    print(rw)

