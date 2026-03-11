# faça seu codigo aqui!
idade = float(input("Digite a idade: "))

if idade < 12:
	conta = 20 + 1.25
	print(round(conta, 2))
elif idade == 12:
	conta = 20 + 2.25
	print(round(conta, 2))
else: 
	conta = 20 + 3.25
	print(round(conta, 2))