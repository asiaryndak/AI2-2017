# AI2-2017
Aplikacje internetowe II


```
=== list1.py ===
match_ends
 OK  got: 3 expected: 3
 OK  got: 2 expected: 2
 OK  got: 1 expected: 1

front_x
 OK  got: ['xaa', 'xzz', 'axx', 'bbb', 'ccc'] expected: ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
 OK  got: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'] expected: ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
 OK  got: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'] expected: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

sort_last
 OK  got: [(2, 1), (3, 2), (1, 3)] expected: [(2, 1), (3, 2), (1, 3)]
 OK  got: [(3, 1), (1, 2), (2, 3)] expected: [(3, 1), (1, 2), (2, 3)]
 OK  got: [(2, 2), (1, 3), (3, 4, 5), (1, 7)] expected: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
>>> 

=== list2.py ===
remove_adjacent
 OK  got: [1, 2, 3] expected: [1, 2, 3]
 OK  got: [2, 3] expected: [2, 3]
 OK  got: [] expected: []
linear_merge
 OK  got: ['aa', 'bb', 'cc', 'xx', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
 OK  got: ['aa', 'bb', 'cc', 'xx', 'zz'] expected: ['aa', 'bb', 'cc', 'xx', 'zz']
 OK  got: ['aa', 'aa', 'aa', 'bb', 'bb'] expected: ['aa', 'aa', 'aa', 'bb', 'bb']
>>> 


=== zadString1.py === 
donuts
  X  got: 'Number of donuts : 4' expected: 'Number of donuts: 4'
  X  got: 'Number of donuts : 9' expected: 'Number of donuts: 9'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
 OK  got: 'Number of donuts: many' expected: 'Number of donuts: many'
both_ends
 OK  got: 'spng' expected: 'spng'
 OK  got: 'Helo' expected: 'Helo'
 OK  got: '' expected: ''
 OK  got: 'xyyz' expected: 'xyyz'
fix_start
 OK  got: 'ba**le' expected: 'ba**le'
 OK  got: 'a*rdv*rk' expected: 'a*rdv*rk'
 OK  got: 'goo*le' expected: 'goo*le'
 OK  got: 'donut' expected: 'donut'
mix_up
 OK  got: 'pox mid' expected: 'pox mid'
 OK  got: 'dig donner' expected: 'dig donner'
  X  got: None expected: 'spash gnort'
  X  got: None expected: 'fizzy perm'
>>> 

===zadString2.py ===
verbing
 OK  got: 'hailing' expected: 'hailing'
 OK  got: 'swimingly' expected: 'swimingly'
 OK  got: 'do' expected: 'do'

not_bad
 OK  got: 'This movie is good' expected: 'This movie is good'
 OK  got: 'This dinner is good!' expected: 'This dinner is good!'
 OK  got: 'This tea is not hot' expected: 'This tea is not hot'
 OK  got: "It's bad yet not" expected: "It's bad yet not"

front_back
 OK  got: 'abxcdy' expected: 'abxcdy'
 OK  got: 'abcxydez' expected: 'abcxydez'
 OK  got: 'KitDontenut' expected: 'KitDontenut'
>>> 


29.03:
gcd:
gcd(10,25):::
5
gcd(14,15):::
1
gcd(3,9):::
3
gcd(1,1):::
1
flip_dict:
flip_dict({CA: US, NY: US, ON: CA})):::
{'US': ['NY', 'CA'], 'CA': ['ON']}
comprehensions:::
[1, 2, 3, 4]
[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
[0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9]
['python']


[None, None, None]
['Y', 'O', 'N']
{8, 2, 3, 5}
comprehensions_write:::
[1, 3, 5, 7]
[True, False, True, False]
['sam', 'guido']
['A', 'O', 'P']
['apple', 'pear']
[('apple', 5), ('orange', 6), ('pear', 4)]
{'pear': 4, 'orange': 6, 'apple': 5}
is_cyclone_phrase:
is_cyclone_phrase('adjourned')
True
is_cyclone_phrase(settled):::
False
is_cyclone_phrase(all alone at noon):::
True
is_cyclone_phrase(by myself at twelve pm):::
False
is_cyclone_phrase('acb'):::
True
is_cyclone_phrase(''):::
True
generate_pascal_row:
generate_pascal_row([1, 2, 1]):::
[1, 3, 3, 1]
generate_pascal_row([]) :::
[1]
generate_pascal_row([1, 4, 6, 4, 1]):::
[1, 5, 10, 10, 5, 1]

is_triangle_number(42):::
False
is_triangle_word('slowo'):::
False
is_triangle_number3
True
is_triangle_number2
False
is_triangle_number9
False
is_triangle_word(word)
False
is_triangle_word(slowo)
False
is_triangle_word(abcd)
True






a: 5
b: 1
c: X
d: None
a: 5
b: 1
c: X
d: None
a: 5
b: 8
c: X
d: None
a: 5
b: 2
c: 4
d: None
a: 5
b: 0
c: 1
d: None
a: 5
b: 2
c: 4
d: 8
a: 1
b: 1
c: 7
d: None
a: 5
b: 2
c: []
d: 5
a: 1
b: 1
c: 7
d: None
>>> 


Positional: (2, 3, 5, 7)
Keyword: {}
Positional: (1, 1)
Keyword: {'n': 1}
Positional: ()
Keyword: {}
Positional: ()
Keyword: {'cs': 'Computer Science', 'pd': 'Product Design'}
Positional: (5, 8)
Keyword: {'k': 1, 'swap': 2}
Positional: (8, 3, 4, 5)
Keyword: {'k': 1, 'a': 5, 'b': 'x'}

10.05.2017 FUNCTIONAL PROGRAMMING

>>> print(function())
[12, -2, 0]
>>> 
=== RESTART: C:/Users/student.INFORMATYKA/Desktop/functionalProgramming.py ===
>>> print(function_length())
[1, 1]
>>> 
=== RESTART: C:/Users/student.INFORMATYKA/Desktop/functionalProgramming.py ===
>>> print(function_length())
[5, 5]

>>> print(function_back())
['olleh', 'dlrow']


>>> print(function_range())
[(2, 4), (3, 27), (4, 256), (5, 3125)]
>>> 
=== RESTART: C:/Users/student.INFORMATYKA/Desktop/functionalProgramming.py ===
>>> print(function_range())
[(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]

>>> 


FILTER:

>>> filtr()
['12', '0']
['world']
['Stanford']
[0, 3, 5, 6, 9, 10, 12, 15, 18]


>>> gcd(9,6)
3
>>> lcm(6,2)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    lcm(6,2)
  File "C:/Users/student.INFORMATYKA/Desktop/functionalProgramming.py", line 41, in lcm
    return functools.reduce(lambda x, y: x * y / gcd(x, y), args)
NameError: name 'functools' is not defined
>>> 
=== RESTART: C:/Users/student.INFORMATYKA/Desktop/functionalProgramming.py ===
>>> lcm(6,2)
6.0
>>> fact(5)
0
>>> 
```
