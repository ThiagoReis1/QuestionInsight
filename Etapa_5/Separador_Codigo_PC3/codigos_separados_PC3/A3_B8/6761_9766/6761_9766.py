# faça seu código aqui!

velocidade = float(input("insira o valor velocidade: "))
custo_total_assinatura = float(input("insira o valor do custo_total_assinatura: "))
custo_fixo = float(input("insira o valor de custo_fixo: "))
assinatura = float(input("digite a assinatura: "))
fixo = float(input("digite o fixo: "))
conta = float(input("digite o valor conta: "))

if velocidade < 50:
	print("4.50")
elif velocidade == 50:
	print("5.50")
elif velocidade > 50:
	print("6.50")
conta = (custo_total + custo_fixo) / 4.00
conta = (custo_total + custo_fixo) / 5.50
conta = (custo_total + custo_fixo) / 6.50

print("valor total")