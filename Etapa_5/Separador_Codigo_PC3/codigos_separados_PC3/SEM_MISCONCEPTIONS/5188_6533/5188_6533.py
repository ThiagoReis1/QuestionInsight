valorr = float(input("Inserir a renda: "))
valorp = float(input("Inserir a prestacao: "))

t = 0.25 * valorr

if(valorp > t):
	print("Emprestimo nao aprovado")
else: 
	print("Emprestimo aprovado")
	