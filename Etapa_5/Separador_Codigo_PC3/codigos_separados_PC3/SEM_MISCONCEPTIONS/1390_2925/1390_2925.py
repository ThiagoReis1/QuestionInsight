from math import*
minutos= int(input("informe minutos falados: "))
tarifa_normal=(minutos*1.20)
tarifa_adicional = ( 25 + 1.40*minutos)

if(minutos < 100 ):
	print(tarifa_normal)
else:(print(round(tarifa_adicional)))
