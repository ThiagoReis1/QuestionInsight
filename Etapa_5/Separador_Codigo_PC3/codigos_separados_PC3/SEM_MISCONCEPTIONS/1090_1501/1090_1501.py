#Universidade Federal do Amazonas
#Maria Luana Crystina de Sousa e Sousa
#Avaliacao 2
#Exercicio 1

compra1 = float(input("qual o valor da 1 compra: "))
compra2 = float(input("qual o valor da 2 compra: "))
compra3 = float(input("qual o valor da 3 compra: "))
compra4 = float(input("qual o valor da 4 compra: "))
limite = float(input("qual o limite do cartao: "))

total = compra1 + compra2 + compra3 + compra4
print(round(total, 2))
if (total <= limite):
	print ("Sim")
else :
	print ("Nao")

