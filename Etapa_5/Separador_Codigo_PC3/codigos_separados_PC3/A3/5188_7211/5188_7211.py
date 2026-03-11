valorrenda=float(input("valor da renda: "))
prestacao =float(input("valor da prestacao: "))

if(prestacao > valorrenda):
	desc=prestacao*0.25
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")
	