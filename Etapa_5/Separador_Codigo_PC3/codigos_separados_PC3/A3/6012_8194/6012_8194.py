ren = float(input("Valor da Renda: "))
pres = float(input("Valor da Prestacao: "))

final = pres *0,25
if ( ren * 0.25 >= pres):
	print("Emprestimo aprovado")
	
else:
	print("Emprestimo nao aprovado")