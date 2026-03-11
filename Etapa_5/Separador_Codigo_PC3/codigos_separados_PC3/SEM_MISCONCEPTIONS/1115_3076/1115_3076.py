salario= float(input())
cdg= int(input())

print("Entradas: R$",salario,"e codigo",cdg)

if(salario>=0)and(cdg==101):
	print("Novo salario: R$",round((salario+(salario*0.008)),2))
elif(salario>=0)and(cdg==102):
		print("Novo salario: R$",round((salario+(salario*0.0065)),2))
elif(salario>=0)and(cdg==103):
		print("Novo salario: R$",round((salario+(salario*0.006)),2))
elif(salario>=0)and(cdg==104):
		print("Novo salario: R$",round((salario+(salario*0.0055)),2))
else: print("Dados invalidos")

