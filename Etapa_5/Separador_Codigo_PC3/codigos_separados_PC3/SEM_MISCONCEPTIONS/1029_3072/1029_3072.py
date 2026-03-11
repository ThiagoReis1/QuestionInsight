a =  0.28 
b = 23
icms = 31

consumo = float(input("digite o consumo de chamadas: "))

valor = (consumo * a) + b
valor_ICMS = valor * (icms / 100)
valor_Total = valor + valor_ICMS

print(round(valor_Total, 2))
