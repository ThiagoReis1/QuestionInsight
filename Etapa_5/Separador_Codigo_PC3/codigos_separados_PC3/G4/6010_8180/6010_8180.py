marcio = float(input("valor da venda: "))
pres = float(input("valor da prestaco: "))
pre = (35/100) * (marcio)
if (pre < pres):
	a = ("Emprestimo nao aprovado")
else:
	a = ("Emprestimo aprovado")
print(a)