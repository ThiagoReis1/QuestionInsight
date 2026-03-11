vr=float(input("valor da renda "))
vp=float(input("valor da prestacao "))
if(vp)>(20/100)*vr:
	mensagem="Emprestimo nao aprovado"
else:
	mensagem="Emprestimo aprovado"
print(mensagem)