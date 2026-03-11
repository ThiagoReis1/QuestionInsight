#Wagner William Amorim de Andrade - 21552149
#Segundo Exercicio Avaliativo
#Questão 1
#30/06/2016

c1 = float(input("Digite o valor da primeira compra: "))
c2 = float(input("Digite o valor da segunda compra: "))
c3 = float(input("Digite o valor da terceira compra: "))
limite = float(input("Digite o valor do limete do cartao da cliente: "))

valor_total = round((c1 + c2 + c3), 2)

if (valor_total <= limite):
		mensagem = "Sim"
else:
		mensagem = "Nao"

print(round((valor_total) , 2))
print(mensagem)