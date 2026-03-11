consumo = float(input()) # Consumo de chamada (em minutos) durante certo mês

Valor = consumo*0.28 + 23 # Valor a ser pago nesse mês

Total = Valor + Valor*0.31 # Valor com imposto ICMS

print(round(Total,2))
