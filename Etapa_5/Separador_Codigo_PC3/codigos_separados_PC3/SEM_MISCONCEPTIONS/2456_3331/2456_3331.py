valor= float(input("valor: "))
filhos= int(input("numero de filhos: "))

r= valor*filhos
r2= r // 100 

if (filhos == 1):
	m= r2 * 10
	print(round(r-m, 2))
elif (filhos == 2):
	m= r2 * 30
	print(round(r-m, 2))
else:
	m= r2 * 40
	print(round(r-m, 2))
