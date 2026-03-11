DF = float(input("digite o valor de renda da Dona Florinda: "))
Prest = float(input("digite o valor da prestacao que pode ser pagada por mes: ")) 
VAR = DF * 0.25 
if(Prest > VAR):
	print("Emprestimo nao aprovado")
else:
	print("Emprestimo aprovado")