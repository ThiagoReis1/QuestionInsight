vr = float(input("o valor de renda: "))
vp = float(input("o valor de prestacao: "))

if(vp <= vr * (15/100)):
	mensagem = "Emprestimo aprovado"
else:
	mensagem = "Emprestimo nao aprovado"
	
print(mensagem)
	