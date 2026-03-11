from math import * 
sqrt(2)

alfa = float(input("digite o angulo de lançamento"))
d = float(input("digite a distancia de lançamento"))
g = 9.8
sena = sin(radians(2 * alfa))
vo = sqrt (d * (g / sena))
			  
print(round(vo,2))