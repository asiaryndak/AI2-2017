def gcd(a, b):
     while b:
        a, b = b, a%b
     return a


def flip_dict(d):
    lista = {}
    for key, value in d.items():
        if value not in lista:
            lista[value] = []
        lista[value].append(key)
    return lista


def comprehensions():
     print([x for x in [1,2,3,4]])#[1, 2, 3, 4]
     print([n-2 for n in range(10)])#[-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
     print([k% 10 for k in range(41) if k%3 ==0])#[0, 3, 6, 9, 2, 5, 8, 1, 4, 7, 0, 3, 6, 9]
     print ([s.lower() for s in ['Python', 'iS','cOoL'] if s[0] <s[-1]])#['python']

     print("\n")
     arr = [[3,2,1], ['a','b','c'], ['do', ['re'], 'mi']]
     print([el.append(el[0] * 4) for el in arr])
     print([letter for letter in "pYthON" if letter.isupper()])
     print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})

def comprehensions_write():
     lista = [0,1,2,3]
     print([2 * num + 1 for num in lista])
     zbior=[3, 5, 9, 8]
     print([num % 3 == 0 for num in zbior])
     napisy=["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
     print([name[3:] for name in napisy if name.startswith('TA_')])
     owoce = ['apple', 'orange', 'pear']
     print([fruit[0].upper() for fruit in owoce])
     print([fruit for fruit in owoce if 'p' in fruit])
     print([(fruit, len(fruit)) for fruit in owoce])
     print({fruit:len(fruit) for fruit in owoce})


def is_cyclone_word(word):
    word = word.upper()
    letters = [None] * len(word)
    half = (len(word) + 1) // 2
    letters[::2] = word[:half]
    letters[1::2] = word[:half - 1:-1]
    return all([left <= right for left, right in zip(letters, letters[1:])])
     
def is_cyclone_phrase(phrase):
     return all([is_cyclone_word(word) for word in phrase.split()])

def generate_pascal_row(row):
    if not row: return [1]
    return [left + right for left, right in zip([0] + row, row + [0])]

print(gcd(10, 25)) # => 5
print(gcd(14, 15)) # => 1
print(gcd(3, 9)) # => 3
print(gcd(1, 1)) # => 1

print(flip_dict({"CA": "US", "NY": "US", "ON": "CA"}))#=> {"US": {"CA", "NY"}, "CA": {"ON"}}
     
comprehensions()
comprehensions_write()

is_cyclone_phrase("adjourned") # => True
is_cyclone_phrase("settled") # => False
is_cyclone_phrase("all alone at noon") # => True
is_cyclone_phrase("by myself at twelve pm") # => False
is_cyclone_phrase("acb") # => True
is_cyclone_phrase("") # => True

generate_pascal_row([1, 2, 1]) #[1, 3, 3, 1]
generate_pascal_row([]) #[1]
generate_pascal_row([1, 4, 6, 4, 1])# [1, 5, 10, 10, 5, 1]
