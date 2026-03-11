s = float(input("Salario atual: "))
c = int(input("codigo do funcionario: "))

print("Entradas: R$",s,"e codigo",c)

if (c==101):
	z = (s*0.0080) + s

	print("Novo salario: R$",round(z,2))
elif (c==102):
	z = (s * 0.0065) + s
	
	print("Novo salario: R$",round(z,2))
elif (c==103):
	z = s*0.0060 + s
	print("Novo salario: R$",round(z,2))
elif (c==104):
	z = (s*0.0055) + s
	
	print("Novo salario: R$",round(z,2))
elif (c!=101) or (c!=102) or (c!=103) or (c!=104):
	print("Dados invalidos")