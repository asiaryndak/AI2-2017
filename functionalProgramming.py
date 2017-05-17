import random       
import functools    
import operator     
import itertools    
import collections  
import inspect 

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


17.05.2017: 
def alpha_score(upper_letters):
    """Computers the alphanumeric sum of letters in a string.
    Prerequisite: upper_letters is composed entirely of capital letters.
    """
    return sum(map(lambda l: 1 + ord(l) - ord('A'), upper_letters))

alpha_score('ABC')  # => 6 = 1 ('A') + 2 ('B') + 3 ('C')

def two_best(words):
    words.sort(key=lambda word: alpha_score(filter(str.isupper, word)), reverse=True)
    return words[:2]

two_best(['hEllO', 'wOrLD', 'i', 'aM', 'PyThOn'])

def printWinner():
    return "Winner"

def printLoser():
    return "Loser"

def printElse():
    return "Tied"


def replacingControlFlow(score):
    return ((score == 1 ) and printWinner()) or ((score == (-1) and printLoser()) or (printElse()))


def iterator_consumption():
    it = iter(range(100))
    67 in it  # => True
    next(it)  # => 68
    37 in it  # => False, and in searching runs the iterator to exhaustion
    next(it)  # => raises StopIteration

def test_itertools():
    for el in itertools.permutations('XKCD', 2):
        print(el, end=', ')
    # ('X', 'K'), ('X', 'C'), ('X', 'D'), \
    # ('K', 'X'), ('K', 'C'), ('K', 'D'), \
    # ('C', 'X'), ('C', 'K'), ('C', 'D'), \
    # ('D', 'X'), ('D', 'K'), ('D', 'C'), \
    
 def dot_product(u, v):
    assert len(u) == len(v)
    return sum(itertools.starmap(operator.mul, zip(u, v)))   


def transpose(m):
    return tuple(zip(*m))

def transpose_lazy(m):
    return zip(*m)

def matmul(m1, m2):
    return tuple(map(lambda row: tuple(dot_product(row, col) for col in transpose(m2)), m1))

def matmul_lazy(m1, m2):
    return map(lambda row: (dot_product(row, col) for col in transpose(m2)), m1)


