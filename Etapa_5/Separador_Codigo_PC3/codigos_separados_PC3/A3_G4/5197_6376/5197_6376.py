vr = float(input("o valor da renda"))
vp = float(input("o valor da prestação"))
vp = vr * (15/100)
if vr >= vp:
	mensagem("emprestimo aprovado")
else:
	mensagem("emprestimo nao aprovado")
print(mensagem)