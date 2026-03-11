salario=float(input("digite o valor do salario"))
codigo=int(input("digite o cod que vc quer"))
print("Entradas: R$" ,salario,"e codigo", codigo )
if(codigo==101):
	Novosalario=(salario*(1+0.008))
	print("Novo salario: R$",(round(Novosalario,2)))
elif(codigo==102):
	Novosalario=(salario*(1+0.0065))
	print("Novo salario: R$",(round(Novosalario,2)))
elif(codigo==103):
	Novosalario=(salario*(1+0.0060))	
	print("Novo salario: R$",(round(Novosalario,2)))
elif(codigo==104):
	NovoSalario=(salario*(1+0.0055))
	print("Novo salario: R$",(round(Novosalario,2)))
else:
	print("Dados invalidos")