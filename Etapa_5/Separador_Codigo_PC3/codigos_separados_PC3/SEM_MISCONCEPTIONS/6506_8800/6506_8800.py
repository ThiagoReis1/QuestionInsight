qnt = int(input("digite a quantidade de refeicoes: "))
caractere = input("digite s ou n: ")
refeicao = 40
if caractere == "s":
	print(qnt * refeicao - (qnt * refeicao * 0.05))
else:
	print(qnt * refeicao)
