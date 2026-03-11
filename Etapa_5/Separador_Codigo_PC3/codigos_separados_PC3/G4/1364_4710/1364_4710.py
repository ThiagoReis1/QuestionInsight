Var1=float(input("Velocidade inicial: "))
Var2=float(input("Distancia: "))
import math
g=9.8
x=math.asin(Var2*g/(Var1**2))*90/math.pi
print(round(x,2))