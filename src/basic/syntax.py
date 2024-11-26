import random

# if-else
var1 = 100
if var1:
    print("var1 true: ", var1)

var2 = 0
if var2:
    print("var2 true: ", var2)
else:
    print("var2 false: ", var2)

for i in range(10):
    random_num = random.randint(1, 100)
    if random_num < 18:
        print("random_num < 18: ", random_num)
    elif 18 < random_num < 27:
        print("random_num < 27: ", random_num)
    elif 27 < random_num < 35:
        print("random_num < 35: ", random_num)
    else:
        print("random_num > 35: ", random_num)


# match-case
def http_err(status):
    match status:
        case "200":
            return "200 OK"
        case "405":
            return "405 Method Not Allowed"
        case "404":
            return "404 Not Found"
        case "500":
            return "500 Internal Server Error"
        case _:
            return "server error"


print(http_err("200"))

# while
my_sum = 0
while my_sum < 100:
    print("sum: ", my_sum)
    my_sum += random.randint(1, 100)
else:
    print("sum: ", my_sum)

# for
list1 = [1, 2, 3]
for item in list1:
    print(item)

word1 = "xiaolu"
for letter in word1:
    print(letter)

for number in range(3):
    print(number)
else:
    print("finished")

# comprehension
names = ['Bob', 'Alice', 'Tom', 'Joe', 'Wendy']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

numbers = [num for num in range(1, 50, 5) if num % 3 == 0]
print(numbers)

new_dict = {key: len(key) for key in names}
print(new_dict)

new_set = {i ** 2 for i in range(3)}
print(new_set)

new_set2 = {x for x in 'csdiciuwebiwbasddcdc' if x not in 'abc'}
print(new_set2)

#  iteration
new_iteration = iter(names)
while True:
    try:
        print(next(new_iteration))
    except StopIteration:
        break


class MyNumbers(object):
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = MyNumbers()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1


generator = countdown(2)
print(next(generator))
print(next(generator))

for value in countdown(3):
    print(value)


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(5)
while True:
    try:
        print(next(f))
    except StopIteration:
        break


# func
def print_info(name, age, gender="F"):
    print(name, age, gender)


print_info("Alice", 18, "M")
print_info(age=18, name="Alice")


# '*' tuple
def print_info(name, *var_tuple):
    print("output: ", name)
    print("var_tuple: ", var_tuple)


print_info("Alice", 18, "M")


# '**' dict
def print_info(name, **var_dict):
    print("output: ", name)
    print("var_dict: ", var_dict)


print_info('Alice', age=18, gender='F')

# lambda
sum1 = lambda x, y: x + y
print("sum: ", sum1(10, 20))


def print_info(a, b, /, d, *, e):
    print("output: ", a, b, d, e)


print_info(1, 2, 3, e=4)

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, nums))
print("nums: ", nums)
print("squared: ", squared)
even_numbers = list(filter(lambda x: x % 2 == 0, nums))
print("even_numbers: ", even_numbers)


# decorator

def before_call():
    print("<<<before call")


def after_call():
    print("after call>>>")


def decorator(func):
    def wrapper(*args, **kwargs):
        # before call new func
        before_call()

        result = func(*args, **kwargs)

        # after call new func
        after_call()

        return result

    return wrapper


@decorator
def print_info(name):
    print(name)


print_info("Alice")


def repeat(n):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return my_decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}")


greet("Alice")


class MyDecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        before_call()
        result = self.func(*args, **kwargs)
        after_call()
        return result

@MyDecorator
def greet2(name):
    print(f"Hello, {name}")

greet2("Xiaolu")