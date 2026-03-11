v_vendas = float(input("Digite o valor de vendas de um funcionario: "))

if (v_vendas <= 1000):
	comissao = (v_vendas * 0.05)
else:
	v_vendas = (1000 * 0.05)
	var = (v_vendas - 1000) * 0.10
	comissao = (v_vendas + var)
print(round(comissao, 2))