r= float(input("valor da renda:"))
p= float(input("valor prestacao:"))

rt= r*(25/100)
if(p>rt):
	msg="Emprestimo nao aprovado"
	
else:
	msg="Emprestimo aprovado"
print(msg)

