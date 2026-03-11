r = float(input("Valor da renda?: "))
p = float(input("Valor da prestacao que pode pagar: "))
if(p>r*15/100):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")