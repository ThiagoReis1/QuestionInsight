#Leitura:
consumo = float(input("Informe o consumo em minutos durante o mes: "))

#Cálculo:
taxa = 0.28
assinatura = 23.00
valor_total = (((taxa * consumo) + (assinatura)) * (31 / 100))

#Impressão:
print(round(valor_total, 2))