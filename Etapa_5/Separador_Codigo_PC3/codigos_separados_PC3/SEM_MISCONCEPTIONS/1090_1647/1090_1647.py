# Universidade Federal do Amazonas
# ICOMP
# Bremer Augusto de Brito Cuesta - 21452666
# Avaliacao 2
# 30

compras_1 = int(input("digite um numero: "))
compras_2 = int(input("digite um numero: "))
compras_3 = int(input("digite um numero: "))
compras_4 = int(input("digite um numero: "))
limite_do_cartao = int(input("digite um numero: "))
valor_total = compras_1 + compras_2 + compras_3 + compras_4 
# Arredondar valores em duas casas decimais

print (round(valor_total, 2))


if (valor_total <= limite_do_cartao):
	mensagem = "sim"
else:
	mensagem = "nao"
print (mensagem)
	


