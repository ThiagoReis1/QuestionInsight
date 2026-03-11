from math import *

Qo = float(input("Valor inicial investido: "))
r = float(input("taxa de rendimento (entre 0.0 e 1.0): "))
Qf = 3 * Qo
y = int(((log(Qf))- log(Qo))/ r)
		  
print(y + 1)