r = float(input("Qual a renda da Dona Florinda?: "))
e = float(input("Qual o valor da prestacao que ela pode pagar?: "))

if(e > 25/100*r):
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")