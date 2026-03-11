qi = int(input("Insira a quantidade inicial de moedas de ouro:\n"))
desp = int(input("Insira a despesa mensal da Coroa:\n"))
M = int(input("Insira a quantidade de moedas coletadas em imposto por mes:\n"))
R = int(input("Insira a quantidade de moedas roubadas por mes\n"))

qtd = qi
mes = 0

while(qtd > 0):
	qtd = qtd + M - (R + desp)
	mes = mes + 1
	
print(mes)