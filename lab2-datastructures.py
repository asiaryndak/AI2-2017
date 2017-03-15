#print ('\n ' , '|', ' ', '|', ' \n', end="---------\n  |   |   \n", flush =False)
#print ('---------\n', end='  |   |   ', flush =False)



def superTictac():
    for x in range (2):
        print(2*'\n  |  |  H  |  |  H  |  |  \n--+--+--H--+--+--H--+--+--', sep='\n', end='\n  |  |  H  |  |  H  |  |  \n========+========+========')
    print(2*'\n  |  |  H  |  |  H  |  |  \n--+--+--H--+--+--H--+--+--',sep='\n', end='\n  |  |  H  |  |  H  |  |  ')


superTictac()


def fizzBuzz():
    suma=0
    x=0
    while(suma<1001):
        if(x%3 == 0 or x%5 ==0):
            suma+=x
            x=x+1
        else:
            x=x+1
    return suma
        
