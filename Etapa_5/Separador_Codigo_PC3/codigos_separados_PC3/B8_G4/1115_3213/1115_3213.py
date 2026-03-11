sal = float(input("Digite salario atual: "))
cod = int(input("Digite o codigo do cargo: "))

print("Entradas: R$", sal, "e codigo", cod )

if (not( cod >= 101 and cod <= 104)):
	print("Dados invalidos")
elif (cod == 101):
	r = (sal * 0.80) / 100
	s = r + sal
	print("Novo salario: R$", round(s, 2))
elif (cod == 102):
	r = (sal * 0.65) / 100
	s = r + sal
	print("Novo salario: R$", round(s, 2))
elif (cod == 103):
	r = (sal * 0.60) / 100
	s = r + sal
	print("Novo salario: R$", round(s, 2))
elif (cod == 104):
	r = (sal * 0.55) / 100
	s = r + sal
	print("Novo salario: R$", round(s, 2))
	