var = float(input("valor da renda: "))
var1 = float(input("valor da prestacao: "))
if(var1 > var*(25/100)):
	print("Emprestimo nao aprovado")
else: 
	print('Emprestimo aprovado')