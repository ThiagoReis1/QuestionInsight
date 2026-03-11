carlos= float(input("valo da renda: "))
presta= float(input("valor da prestacao: "))
per= (20/100)*carlos
if(per<presta):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")