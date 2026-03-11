from math import*

f = float(input("funcao: "))

if f>=-4 and f<0:
	f1= abs(f**(1/2))
	print(round(f1, 4))
elif f>=0 and f<=4:
	f1= abs(f**(1/2))
	print(round(f1, 4))
else:
	print("entrada invalida")