renda= float(input("Qual o valor da renda? "))
prestacao= float(input("Qual o valor da prestacao? "))

#emprestimo
if(prestacao > renda * 0.25):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")