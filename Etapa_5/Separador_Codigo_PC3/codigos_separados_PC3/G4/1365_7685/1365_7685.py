import math
ang= math.radians(float(input("angulo da flecha: ")))
d= float(input("distancia entre voce e a criatura: "))
g= 9.8

v= (d*g/math.sin(2*ang))**(1/2)
								  
print(round(v, 2))