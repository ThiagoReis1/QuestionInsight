v_renda = float(input())
v_prest = float(input())

valor_p = (v_renda * 35/100)
if v_prest > valor_p :
	msg = "Emprestimo nao aprovado"
else:
	msg = "Emprestimo aprovado"

print(msg)