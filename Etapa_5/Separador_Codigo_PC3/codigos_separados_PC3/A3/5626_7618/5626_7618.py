renda=float(input("digite  renda= "))
prestacao=float(input("digite a prestacao= "))

total= (renda + prestacao)+ (prestacao * 0.25)

if (renda * 0.25 < prestacao) :

	print("Emprestimo nao aprovado")
else :
	print("Emprestimo aprovado")
	