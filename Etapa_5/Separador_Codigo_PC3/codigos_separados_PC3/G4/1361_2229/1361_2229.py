#poção para resistir ao fogo#

#necessario
from math import*

#entrada
pocao=int(input("quantas pocoes: "))

#formulas
sn=((sqrt(5)-1)/4)*pocao
sa=(sqrt(5-(2*sqrt(5))))*pocao
am=(5*(5-(2*sqrt(5))))*pocao
			  
#impressão
print(round(sn,2))
print(round(sa,2))
print(round(am,2))			  