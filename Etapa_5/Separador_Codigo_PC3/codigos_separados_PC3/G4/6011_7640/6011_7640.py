v = float(input("Valor da renda: "))
v_p = float(input("Valor da prestacao: ")) 

conta = v * (35/100)

if(v_p > conta):
	em = "Emprestimo nao aprovado"
else: 
	em = "Emprestimo aprovado"
	
print(em)