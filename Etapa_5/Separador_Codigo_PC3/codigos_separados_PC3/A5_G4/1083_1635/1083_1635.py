import math

x = float(input("digite a nota 1: "))
y = float(input("digite a nota 2: "))
z = float(input("digite a nota 3: "))

#calculo das medias das notas 
a = (x+y+z)/3
 

if a > 6:
	print(round(a), 2)
	print("aprovacao")
	
else:
	print(round(a), 2) 
	print("reprovacao")
	