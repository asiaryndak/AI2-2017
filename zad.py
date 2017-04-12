
import math
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


def is_triangle_number(num):
    discrim = 8 * num + 1
    base = int(math.sqrt(discrim))
    return base * base == discrim


def is_triangle_word(word):
    count = 0
    for ch in word.upper().strip():
        count += ord(ch) - ord('A') + 1
    return is_triangle_number(count)


def triangle_words():
    with open('/usr/share/dict/words', 'r') as f:
        lines = f.readlines()

    triangle_words = {line.upper().strip() for line in lines if is_triangle_word(line)}
    return len(triangle_words)


def polygon_collision(poly1, poly2):
    pass  #


print("gcd:")
print("gcd(10,25):::")
print(gcd(10, 25)) # => 5
print("gcd(14,15):::")
print(gcd(14, 15)) # => 1
print("gcd(3,9):::")
print(gcd(3, 9)) # => 3
print("gcd(1,1):::")
print(gcd(1, 1)) # => 1

print("flip_dict:")
print("flip_dict({CA: US, NY: US, ON: CA})):::")

print(flip_dict({"CA": "US", "NY": "US", "ON": "CA"}))#=> {"US": {"CA", "NY"}, "CA": {"ON"}}

print("comprehensions:::")     
comprehensions()
print("comprehensions_write:::")
comprehensions_write()

print("is_cyclone_phrase:")
print("is_cyclone_phrase('adjourned')")

print(is_cyclone_phrase("adjourned")) # => True
print("is_cyclone_phrase(settled):::")
print(is_cyclone_phrase("settled")) # => False
print("is_cyclone_phrase(all alone at noon):::")
print(is_cyclone_phrase("all alone at noon")) # => True
print("is_cyclone_phrase(by myself at twelve pm):::")
print(is_cyclone_phrase("by myself at twelve pm")) # => False
print("is_cyclone_phrase('acb'):::")
print(is_cyclone_phrase("acb")) # => True
print("is_cyclone_phrase(''):::")
print(is_cyclone_phrase("")) # => True

print("generate_pascal_row:")
print("generate_pascal_row([1, 2, 1]):::")
print(generate_pascal_row([1, 2, 1])) #[1, 3, 3, 1]
print("generate_pascal_row([]) :::")
print(generate_pascal_row([])) #[1]
print("generate_pascal_row([1, 4, 6, 4, 1]):::")
print(generate_pascal_row([1, 4, 6, 4, 1]))# [1, 5, 10, 10, 5, 1]


print("is_triangle_number(42):::")
print(is_triangle_number(52))
print("is_triangle_word('slowo'):::")
print(is_triangle_word("slowo"))
#print("triangle_words():::")
#print(triangle_words())
#print("polygon_collision(poly1, poly2):::")
#print(polygon_collision(poly1, poly2))


