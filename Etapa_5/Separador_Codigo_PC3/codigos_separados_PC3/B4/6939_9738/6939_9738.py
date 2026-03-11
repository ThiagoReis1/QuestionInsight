valor= float(input())
opcao= input().upper()

if opcao == "D":
	desconto= valor*(19/100)
	total= valor- desconto
	print(round(total,2))
	
elif opcao == "P":
	desconto= valor * (19/100)
	total= valor-desconto
	print(round(total,2))
	
else:
	vezes= int(input())
	if vezes == 1:
		print(valor)
	else:
		juros= valor*(9/100)
		total= valor+ juros
		print(round(total,2))