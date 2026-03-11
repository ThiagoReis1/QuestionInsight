vr = float(input("valor da renda: "))
vp = float(input("valor da prestacao: "))

ex = vr * (15/100)

if vp > ex:
	mensagem = "Emprestimo nao aprovado"
else:
	mensagem = "Emprestimo aprovado"
	
print(mensagem)