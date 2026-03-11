from math import *

Qo = float(input('digite o valor investido  '))
Qf = float(input('digite o valor pretendido  '))
y = float(input('digite a duração do investimento '))

r = (log(Qf) - log(Qo)) / y
			 
print(r)