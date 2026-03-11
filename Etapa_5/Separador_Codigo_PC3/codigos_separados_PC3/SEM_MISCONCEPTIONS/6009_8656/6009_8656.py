renda= float(input("valor da renda: ")) 
prestacao= float(input("valor da prestacao: "))

r1= renda * 30/100

if(prestacao > r1):
	print("Emprestimo nao aprovado")
	
else:
	print("Emprestimo aprovado")
	