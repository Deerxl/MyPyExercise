"""
this is a kind of notes
"""
import operator
from collections import deque
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

# list
list1 = [1, 2, 3]
list2 = ["Google", "Facebook", "Twitter", "Linkedin", "Apple"]

print("list1:", list1)
print("list2:", list2)

# modify
list1[0] = 0
print(list1)

# append
list1.append(4)
print(list1)

# del
list1.remove(2)
print(list1)

# combine
list1 += list2
print(list1)

# nesting
list3 = [list1, list2]
print(list3)
print(list3[0][3])

# compare
print("operator.eq(list1[0], list2[0]): ", operator.eq(list1[0], list2[0]))

# statics
list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0]
print("len(list1)", len(list1))
print("max(list1)", max(list1))
print("min(list1)", min(list1))
print("sum(list1)", sum(list1))

# tuple
tuple1 = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0)
print("id(tuple1): ", id(tuple1))
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("id(tuple1): ", id(tuple1))


# dict
dict1 = {"key1": 1, "key2": 2, "key3": 3}
print("dict1: ", dict1)
dict1["key4"] = 4
print("dict1: ", dict1)
dict1.pop("key4")
print("dict1: ", dict1)
del dict1["key3"]
print("dict1: ", dict1)
dict1.keys()
dict1.clear()
print("dict1: ", dict1)

# set
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("set1: ", set1)
set1.remove(4)
print("set1: ", set1)
# set1.remove(10) # error no key exist
print("set1: ", set1)
set1.pop() # random remove one element
print("set1: ", set1)
set1.discard(10)
print("set1: ", set1)

set2 = set(list2)
print("set2: ", set2)
set2.update({"Microsoft", "Google"})
print("set2: ", set2)
set2.update(["Zoom", "Tencent"])
print("set2: ", set2)


# queue
my_queue = deque([1, 2, 3])

# push
my_queue.append(4)
my_queue.append(5)
print("my_queue: ", my_queue)
# pop
my_queue.popleft()
# first ele
first_ele = my_queue[0]
print("first_ele: ", first_ele)
# is empty
is_empty = my_queue == []
print("is_empty: ", is_empty)
# size
queue_size = len(my_queue)
print("queue_size: ", queue_size)

# stack
my_stack = [0, 1, 2, 3, 4]
print("my_stack: ", my_stack)
# push
my_stack.append(5)
print("my_stack: ", my_stack)
top_ele = my_stack.pop()
print("top_ele: ", top_ele)
print("my_stack: ", my_stack)
# peek
peek_ele = my_stack[-1]
print("peek_ele: ", peek_ele)
stack_is_empty = len(my_stack) == 0
print("stack_is_empty: ", stack_is_empty)

# comprehension
vec1 = [1, 2, 3]
vec2 = [x**2 for x in vec1]
print("vec1: ", vec1)
print("vec2: ", vec2)
vec3 = [[x, x**2] for x in vec1]
print("vec3: ", vec3)

for i, v in enumerate(vec1):
    print(i, v)

fruit_vec = [' apple ', ' banana ', ' orange ']
print("fruit_vec: ", fruit_vec)
new_fruit_vec = [x.strip() for x in fruit_vec]
print("new_fruit_vec: ", new_fruit_vec)

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print("matrix: ", matrix)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print("transposed: ", transposed)

tuple1 = 1, 2, 3
print("tuple1: ", tuple1)
tuple2 = tuple1, ('Hello', 'World')
print("tuple2: ", tuple2)

# dict
dict1 = {"key1": 1, "key2": 2, "key3": 3}
print("dict1: ", dict1)
for key, value in dict1.items():
    print(key, value)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for question, answer in zip(questions, answers):
    print("What is your {0}? It is {1}.".format(question, answer))

if __name__ == "__main__":
    input = 'I like xiaolu'
    rw = reverse_words(input)
    print(rw)

