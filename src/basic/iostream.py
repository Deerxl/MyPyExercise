import datetime
import math
import pickle
import pprint

s = 'hello, world'

print(str(s))
print(repr(s))
print(s.encode())
print(1 / 7)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# zfill
print('-3.14'.zfill(7))
print('3.14'.zfill(5))

print('Hello, {}, nice to meet you! Today is {}'.format('xiaolu', datetime.datetime.now()))

print('PI\'s value is similar to {0:.3f}'.format(math.pi))

my_table = {'Google': 1, 'Apple': 2, 'Microsoft': 3}
for key, value in my_table.items():
    print('{0:10} ===========> {1:10d} '.format(key, value))


# file read and write
f = open('source/test.txt', 'w')
f.write('Hello, {}, nice to meet you! \nNow is {}'.format('Xiaolu', datetime.datetime.now()))
f.close()

f = open('source/test.txt', 'r')
file_content = f.read()
print(file_content)
f.close()


f = open('source/test.txt', 'r')
string2 = f.readline(5)
print(string2)

string3 = f.readlines()
print(string3)
f.close()



# pickle
output_data = open('source/testdata.pkl', 'wb')
data1 = {'a': [1, 2.0, 4+3.2j],
         'b': ('string', u'Unicode text'),
         'c':None}
# Pickle dictionary using protocol 0.
pickle.dump(data1, output_data)

self_ref_list = [1, 2, 3]
self_ref_list.append(self_ref_list)

# Pickle the list using the highest protocol available.
pickle.dump(self_ref_list, output_data, -1)

output_data.close()


pkl_file = open('source/testdata.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()
