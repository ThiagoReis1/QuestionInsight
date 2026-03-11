renda = float(input())
v_p = float(input())
valor = renda * 35/100

if v_p > valor:
	msg = "Emprestimo nao aprovado"
else:
	msg = "Emprestimo aprovado"
	
print(msg)