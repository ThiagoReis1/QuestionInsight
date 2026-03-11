unidade=input("A ou H?: ")
valor=float(input())
				
if (unidade=="A"):
	hect=(valor)/(2.47105)
	print(round(hect,2))
else:
	acre=(2.47105)*valor
	print(round(acre,2))			
				