ent = input()		#entrada

ala = 3*12.011 + 7*1.00794 + 1*14.00674 + 2*15.9994		#calculo alanina
val = 5*12.011 + 11*1.00794 + 1*14.00674 + 2*15.9994		#calculo valina

A = (ent.upper())		#conversões de entrada
B = (ent.upper())

if A == "ALANINA":
	print(round(ala,2))
	
if B == "VALINA":
	print(round(val,2))

