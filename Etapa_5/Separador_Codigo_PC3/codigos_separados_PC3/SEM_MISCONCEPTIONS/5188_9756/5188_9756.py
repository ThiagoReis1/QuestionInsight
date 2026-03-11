renda = float(input("Dona Florinda me informe sua renda: "))
parcela = float(input("Qual valor da parcela mensal a senhora pode pagar?: "))

if parcela > (25/100)*renda:
	print ("Emprestimo nao aprovado")
	
else: 
	print ("Emprestimo aprovado")