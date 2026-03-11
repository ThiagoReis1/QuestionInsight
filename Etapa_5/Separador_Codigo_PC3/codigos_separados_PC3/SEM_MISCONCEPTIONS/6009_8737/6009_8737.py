vr = float(input('digite a renda :'))
vp = float(input('digite o valor da prestacaoo :'))

porcentagem = (vr * (30/100))

if vp >= porcentagem :
	print ('Emprestimo nao aprovado')
	
else :
	print("Emprestimo aprovado")