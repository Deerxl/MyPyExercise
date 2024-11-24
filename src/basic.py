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
str = "12345678"
print("str.len", len(str))
print("str[0: 5]", str[0: 5])
print("str[0: -1]", str[0: -1]) # -1 represents the last index of the str
print("str[0: -3]", str[0: -3]) # -3 represents the third index of the str from the right
print("str[0: 10]", str[0: 10])
print("str[0: 9]", str[0: len(str) + 1])
print("str[3:]", str[3:])
print("str[:3]", str[:3])
print("str*2", str * 2)

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

# list
my_list = [1, 2, 'a', 3.5, True, 3]
print(my_list)
my_list[0] = 'xiaolu'
print(my_list)
my_list[2:4] = []
print(my_list)
print(my_list * 2)


def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[::-1]
    output = " ".join(inputWords)
    return output



if __name__ == "__main__":
    input = 'I like xiaolu'
    rw = reverseWords(input)
    print(rw)

