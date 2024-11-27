import doctest
import glob
import itertools
import math
import os
import random
import re
import shutil
import sys
from datetime import datetime
from urllib.error import HTTPError
from urllib.request import urlopen

# os
cur_dir = os.getcwd()
print("cur_dir:", cur_dir)
files = os.listdir(cur_dir)
print("files:", files)

print(dir(os))
# help(os)

# shutil
shutil.copy('source/test.txt', 'source/test1.txt')

# glob
print(glob.glob('source/*.txt'))

# sys
print(sys.argv)

# re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

# math
print(math.cos(math.pi / 4))

# random
my_choice = random.choice(['a', 'b', 'c'])
print(my_choice)

samples = random.sample(range(100), 10)
print(samples)

print(random.random())
print(random.randrange(1, 10))

# url
try:
    for line in urlopen("http://baidu.com"):
        lin = line.decode('utf-8')
        print(lin)
except HTTPError as e:
    print(e.code, e.reason)
    pass

# datetime
cur_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(cur_time)

cur_day = datetime.now().strftime('%Y-%m-%d')
print(cur_day)

def cal_avr(values):
    return sum(values) / len(values)


doctest.testmod()


# cartesian
class Cartesian(object):
    def __init__(self):
        self._data_list = []

    def add_data(self, data=None):
        if data is None:
            data = []
        self._data_list.append(data)

    def build(self):
        for item in itertools.product(*self._data_list):
            print(item)

car = Cartesian()
car.add_data([1, 2, 3])
car.add_data([4, 5, 6])
car.build()
