x=float(input("salario_atual: "))
y=int(input("codigo: "))

print("Entradas: R$",x,"e codigo",y)

if(y==101):
	a=x*(0.8/100)
	print("Novo salario: R$",round(x+a,2))
elif(y==102):
	a=x*(0.65/100)
	print("Novo salario: R$",round(x+a,2))
elif(y==103):
	a=x*(0.60/100)
	print("Novo salario: R$",round(x+a,2))
elif(y==104):
	a=x*(0.55/100)
	print("Novo salario: R$",round(x+a,2))
else:
	print("Dados invalidos")