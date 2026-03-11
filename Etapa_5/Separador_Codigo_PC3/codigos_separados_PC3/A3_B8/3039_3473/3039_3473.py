import math as mt
x = float(input())

saida = "entrada invalida"

if( (-1 <= x and x<-0.5) or (0.5 < x and x <= 1) ):
	saida = mt.degrees(mt.asin(x))
	saida = round(saida,2)
elif( -0.5 <= x and x <= 0.5):
	saida = mt.degrees(mt.acos(x))
	saida = round(saida,2)

print(saida)