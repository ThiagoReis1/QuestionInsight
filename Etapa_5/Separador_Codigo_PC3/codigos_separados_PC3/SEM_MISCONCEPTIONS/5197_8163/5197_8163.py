r= float(input('valor da renda do seu madruga: '))
p= float(input('valor da prestacao por mes: '))

if p > r*(20/100):
	mensagem= "Emprestimo nao aprovado"
else:
	mensagem= "Emprestimo aprovado"
	
print(mensagem)