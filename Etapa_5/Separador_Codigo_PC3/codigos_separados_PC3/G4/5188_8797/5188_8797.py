a = float(input("valor da renda "))
b = float(input("valor da prestacao"))

v = a * 25/100

if b > v: 
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")