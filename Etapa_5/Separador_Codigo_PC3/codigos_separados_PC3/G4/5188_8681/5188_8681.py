vr = float(input("Insira o valor da renda: "))
vp = float(input("Insira o valor da prestacao: "))

a = 25/100
b = vr*a

if (vp > b):
	msg = "Emprestimo nao aprovado"
else:
	msg = "Emprestimo aprovado"
	
print(msg)