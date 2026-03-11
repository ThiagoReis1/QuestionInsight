vr = float(input("O valor de renda: "))
vp = float(input("O valor de prestacao: "))

if (vp > vr * (20/100)):
	mensagem = "Emprestimo nao aprovado"
else:
	mensagem = "Emprestimo aprovado"
	
print(mensagem)