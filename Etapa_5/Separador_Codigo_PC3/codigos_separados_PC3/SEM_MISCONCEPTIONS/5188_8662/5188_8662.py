v_renda = float(input('Digite o valor da renda: '))
v_prestacao = float(input('Digite o valor da prestacao: '))

if v_prestacao > v_renda * 0.25:
	msg = 'Emprestimo nao aprovado'
else:
	msg = 'Emprestimo aprovado'

print(msg)