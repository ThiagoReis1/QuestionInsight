from math import *

qo = float(input("Valor inicial: "))
r = int(input("Taxa rendimento: "))


y = float((log(3*qo)) - (log(qo))) / r
	  
print(int(y))