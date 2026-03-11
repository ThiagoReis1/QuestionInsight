kWh = 0.43
fixo = 10

conta = float(input('valor da conta: '))

valor = (conta * kWh) + fixo
icms = (valor * 25 /100)

total = valor + icms 

print(round(total, 2))