vr = float(input("Qual o valor da renda?"))
vp = float(input("Qual o valor da prestacao?"))

if (vp > (vr * 15/100)):
	msg = "Emprestimo nao aprovado"
else:
	msg = "Emprestimo aprovado"
print(msg)