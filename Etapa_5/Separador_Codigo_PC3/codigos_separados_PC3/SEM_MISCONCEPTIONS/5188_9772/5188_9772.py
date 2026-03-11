renda= float(input( "insira valor da renda: "))
prest=float(input("insira o valor da prestacao: "))
parcela= renda * 0.25
if prest <= parcela: 
	msg = "Emprestimo aprovado"
else :
	msg= "Emprestimo nao aprovado"

print(msg)