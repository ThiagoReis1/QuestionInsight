vr=float(input("valor de renda de marcio: "))
vp=float(input("valor da prestacao: "))

m=vr*(35/100)

if vp >=  m:
	mensagem = "Emprestimo nao aprovado"
else:
	mensagem = "Emprestimo aprovado"
	
print(mensagem)