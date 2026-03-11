sal=float(input())
cod=int(input())
adm=sal+(sal*(0.8/100)
eng=sal+(sal*(0.65/100)
med=sal+(sal*(0.6/100)
o=sal+(sal*(0.55/100)
if ((sal<0)and (cod!= 101 or cod!= 101 or cod!= 101 or cod!= 101)) :
	print("Entradas: R$",sal, "e codigo",cod)
	print("Dados invalidos")
else :
	if (cod == 101) :
		print("Entradas: R$",sal, "e codigo",cod)
		print("Novo salario: R$",adm)
	elif (cod == 102):
		print("Entradas: R$",sal ,"e codigo",cod)
		print("Novo salario: R$",eng)
	elif (cod == 103) :
		print("Entradas: R$",sal, "e codigo",cod)
		print("Novo salario: R$",med)
	else :
		print("Entradas: R$",sal, "e codigo",cod)
		print("Novo salario: R$",o)