from math import *
molecula = input("Digite o nome do aminoácido: ")

glutamina = (5*12.011) + (8*1.00794) + (1*14.0067) + (4*15.9994)
treonina =  (4*12.011) + (9*1.00794) + (1*14.0067) + (3*15.9994)

if(molecula.upper() == "GLUTAMINA"):
	print(round(glutamina, 2))
else:
	print(round(treonina, 2))