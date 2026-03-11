sal = float(input("Qual o valor de salario atual? "))
cod = int(input("Qual o codigo do funcionario? "))

if (cod == 101):
	nsal = ((0.80/100) * sal) + sal
elif (cod == 102): 
	nsal = ((0.65/100) * sal) + sal
elif (cod == 103):
	nsal = ((0.60/100) * sal) + sal
elif (cod == 104):
	nsal = ((0.55/100) * sal) + sal	

print(round("Novo salario: R$", nsal, 2))