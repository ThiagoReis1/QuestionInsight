from math import *

x = float(input('informe o valor de x: '))
valor = 0
if (x < -4) or (x > 4):
    print('entrada invalida')
else:
    if (x >= -4) and (x < 0):
        valor = (abs(x)) ** (1/2)
        print(round(valor, 4))
#    print(valor)
    elif (x >= 0) and (x <= 4):
        valor = x ** (1/2)
        print(round(valor ,4))
			#    print(valor)		
#else:
    #print('entrada invalida')
#print(round(valor, 4))