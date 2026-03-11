from math import *

x = int(input("Digite x: "))
funcao = f(x)

if ((x < -1 and x >= -1/2) or (x < -1/2 and x > 1/2)):
	 print("entrada invalida")
elif (x >= -1 and x < -1/2):
	 print(funcao == asin(x))
elif (x >= -1/2 and x <= 1/2):
	 print(funcao == degrees(acos(x))