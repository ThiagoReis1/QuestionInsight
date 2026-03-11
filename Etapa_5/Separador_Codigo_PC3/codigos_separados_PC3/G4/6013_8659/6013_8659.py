vr = float(input("o valor da renda: "))
vp = float(input("o valor da prestacao: "))
ex = vr * (15/100)
if vp > ex:
	mensagem = "Emprestimo nao aprovado"
else:
	mensagem = "Emprestimo aprovado"
	
print(mensagem)