#print ('\n ' , '|', ' ', '|', ' \n', end="---------\n  |   |   \n", flush =False)
#print ('---------\n', end='  |   |   ', flush =False)



def superTictac():
    for x in range (2):
        print(2*'\n  |  |  H  |  |  H  |  |  \n--+--+--H--+--+--H--+--+--', sep='\n', end='\n  |  |  H  |  |  H  |  |  \n========+========+========')
    print(2*'\n  |  |  H  |  |  H  |  |  \n--+--+--H--+--+--H--+--+--',sep='\n', end='\n  |  |  H  |  |  H  |  |  ')


def fizzbuzz():
    suma = 0
    for num in range (1000):
        if (num % 3) == 0:
            if (suma + num) > 1001:
                break
            else:
                suma += num
        elif (num % 5) == 0:
            if (suma + num) > 1001:
                break
            else:
                suma += num
    return suma



def collatz(y):
    lista = []
    while(y>1):
        if(y%2 == 0 ):
            y=y/2
            lista.append(int(y))
        elif(y%2 !=0):
            y= 3*y +1
            lista.append(int(y))
    return lista
    
        
def converter():
    temp = float(input("Podaj temperaturę w stopniach Fahrenheit'a"))
    tempC = (temp-32)/1.8
    print (tempC)


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
