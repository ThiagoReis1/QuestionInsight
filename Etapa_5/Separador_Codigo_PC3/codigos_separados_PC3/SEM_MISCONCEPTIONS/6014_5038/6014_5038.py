renda = float(input("valor da renda: "))
prestacao = float(input("valor da prestacao: "))
renda2 = renda*(35/100)
if(prestacao>renda2):
	msg = "Emprestimo nao aprovado"
else:
	msg = "Emprestimo aprovado"
print(msg)