from math import *

x = 0.37
y = 15.0
z = 35/100
vol = float(input("entre com o volume da agua: "))
custo = vol * x + y
custotot = custo * z
			
print(round(custo + custotot,2))