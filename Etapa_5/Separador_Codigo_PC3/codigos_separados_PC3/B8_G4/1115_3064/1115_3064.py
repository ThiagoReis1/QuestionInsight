x= float(input("Digite o salario atual: "))
y= int(input("Digite o codigo do cargo: "))
print("Entradas: R$",x,"e codigo",y)
if (x<=0)or((y!=101)and(y!=102)and(y!=103)and(y!=104)):
	print("Dados invalidos")
elif (y==103):
	z= (x*(0.006))+x
	print("Novo salario: R$",round(z,2))
elif  (y==101):
	z= (x*(0.008))+x
	print("Novo salario: R$",round(z,2))	
elif  (y==102):
	z= (x*(0.0065))+x
	print("Novo salario: R$",round(z,2))	
elif  (y==104):
	z= (x*(0.0055))+x
	print("Novo salario: R$",round(z,2))	