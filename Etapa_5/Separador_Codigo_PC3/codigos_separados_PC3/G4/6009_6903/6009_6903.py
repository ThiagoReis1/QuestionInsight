vr = float(input("valor da renda da Dona Fernanda: "))
em = float(input("valor da prestacao que ela pagara por mes: "))
 
t = 0.3*vr
if t > em:
	print("Emprestimo aprovado")
else:
	print("Emprestimo nao aprovado")