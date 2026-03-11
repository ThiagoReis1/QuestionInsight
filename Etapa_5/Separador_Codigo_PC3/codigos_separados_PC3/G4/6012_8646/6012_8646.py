sal = float(input("Salario: "))
pre = float(input("Prestacao: "))

op = sal*0.25

if pre > op:
	print("Emprestimo nao aprovado")

else:
	print("Emprestimo aprovado")