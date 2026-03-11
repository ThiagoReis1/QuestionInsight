acai=int(input("qual as gramas do acai?"))
salgado=int(input("qual a quantidade de salgados?"))
pagamento=float(input("qual valor pago"))
total=(salgado*3)+(acai*(24/1000))
if(pagamento>total):
	print(round(total,2))
	print("Sim")
else:
	print(round(total,2))
	print("Nao")