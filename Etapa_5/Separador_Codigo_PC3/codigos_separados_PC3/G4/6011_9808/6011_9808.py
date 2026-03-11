r = float(input("Valor de renda da dona Carla: "))
p = float(input("Valor da prestacao que ela pode pagar po mes: "))

if p < r*0.35:
	print ("Emprestimo aprovado")
	
else: 
	print("Emprestimo nao aprovado")