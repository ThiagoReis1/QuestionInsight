num_1=float(input("Valor da compra 1 "))
num_2=float(input("Valor da compra 2 "))
num_3=float(input("Valor da compra 3 "))
num_4=float(input("Valor da compra 4 "))
limite=float(input("Limite"))
transacao_=num_1+num_2+num_3+num_4
if (transacao_<=limite):
	mensagem= "Sim"
else:
	mensagem= "Nao"
print(round(transacao_, 2))
print(mensagem)