#Universidade Federal do Amazonas
#Jorge Trajano da Silva Junior - 21553770
#Avaliação 04 - Exercício 01
#05/08/2016
vlr = int(input("Informe o valor do prêmio: R$"))
tp = float(input("Informe a taxa de rendimento da poupança: "))
vm = int(input("Informe o valor esbanjado mensalmente: "))
meses = 0
g = vlr
while(g > 0):
	g = g + (g*tp/100)-vm
	meses = meses+1
print(meses)