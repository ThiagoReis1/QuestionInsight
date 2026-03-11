renda = float(input("insira a renda da dona florinda: "))
pres = float(input('insira o valor da prestacao: '))

parcela = renda * .25

if pres > parcela:
	msg = "Emprestimo nao aprovado"
else:
	msg = "Emprestimo aprovado"
	
print(msg)