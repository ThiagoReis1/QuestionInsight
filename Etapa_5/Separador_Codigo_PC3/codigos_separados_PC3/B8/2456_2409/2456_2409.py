mensalidade = float(input("qual o valor da mensalidade? "))
crianca = int(input("quantas criancas? "))

if(crianca == 1):
	desconto = (mensalidade * 0.1)
elif(crianca == 2):
	desconto = (mensalidade * 0.3)
elif(crianca >= 3):
	desconto = (mensalidade * 0.4)

valor_total = crianca * (mensalidade - desconto)
print(round(valor_total, 2))