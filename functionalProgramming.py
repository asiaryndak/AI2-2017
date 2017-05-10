

(lambda val: val ** 2)(5)  # => 25
(lambda x, y: x * y)(3, 8)  # => 24
(lambda s: s.strip().lower()[:2])('  PyTHon')  # => 'py'

def function_int():
    #print(['12', '-2', '0'] ----->  [12, -2, 0])
    return list(map(int,['12','-2','0']))

def function_length():
    return list(map(len,(['hello','world'])))
    
def function_back():
    return list(map(lambda s: s[::-1], ['hello', 'world']))

def function_range():
    return list(map(lambda x : (x,x**2,x**3),range(2,6)))

#def function_zip():
    #return list(map(lambda l, r : (l*r), zip(range(2, 5), range(3, 9, 2))))


def filtr():
    # ['12', '-2', '0'] -> ['12', '0']
    print(list(filter(lambda x: int(x) >= 0, ['12', '-2', '0'])))
    # ['hello', 'world'] -> ['world']
    print(list(filter(lambda x: x == 'world', ['hello', 'world'])))
    # ['Stanford', 'Cal', 'UCLA'] -> ['Stanford']
    print(list(filter(lambda x: x[0] == 'S', ['Stanford', 'Cal', 'UCLA'])))
    # range(20) -> [0, 3, 5, 6, 9, 10, 12, 15, 18]
    print(list(filter(lambda n: n % 3 == 0 or n % 5 == 0, range(20))))

    def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*args):
    return functools.reduce(lambda x, y: x * y / gcd(x, y), args)

def fact(n):
    return functools.reduce(operator.mul, range(n))

