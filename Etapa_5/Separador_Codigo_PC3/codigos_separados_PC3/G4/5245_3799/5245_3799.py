s=float(input("salario:"))
print("Entrada: R$",s)
if(s<0):
	print("Dado invalido")
elif(0>s and s<=800):
	x=0.50
	y=round((s+(s*x)),2)
	print("Novo salario: R$",y)
elif(s>800 and s<=1000):
	x=0.40
	y=round((s+(s*x)),2)
	print("Novo salario: R$",y)
elif(s<=1200):
	x=0.30
	y=round((s+(s*x)),2)
	print("Novo salario: R$",y)
elif(s<1400):
	x=0.20
	y=round((s+(s*x)),2)
	print("Novo salario: R$",y)
elif(s<=1600):
	x=0.10
	y=round((s+(s*x)),2)
	print("Novo salario: R$",y)
else:
	x=0.05
	y=round((s+(s*x)),2)
	print("Novo salario: R$",y)
