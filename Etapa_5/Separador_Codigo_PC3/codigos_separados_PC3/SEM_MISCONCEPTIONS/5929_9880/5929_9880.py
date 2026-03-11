#Inserindo dados de consumo
vol_cons = float(input("Qual o volume de agua consumida?: "))

#Calculando o valor a ser pago
ICMS = 0.35
valor_pago = vol_cons * 0.37 + 15.00
valor_total = valor_pago + valor_pago * ICMS 

#Imprimindo valor total a ser pago
print(round(valor_total, 2))
