renda = float(input('insira o valor da renda: '))
pres = float(input('insira o valor da prestacao: '))

if pres > renda *(35/100):
	msg = "Emprestimo nao aprovado"
else:
	msg = "Emprestimo aprovado"
print(msg)
	