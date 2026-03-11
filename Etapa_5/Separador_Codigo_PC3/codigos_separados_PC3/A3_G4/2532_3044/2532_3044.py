x=float(input("carro: "))
y=float(input("valor inicial: "))
z=float(input("valor fixo: "))
w=float(input("juros: "))
qi=y
a=0
if(x>0 and y>0 and z>0 and w>0):
	while(qi<x):
		qi=qi+(qi*(w/100))+z
		a=a+1		
		s=round(qi,2)
	print(a)
else:
	print("Dados incorretos")
