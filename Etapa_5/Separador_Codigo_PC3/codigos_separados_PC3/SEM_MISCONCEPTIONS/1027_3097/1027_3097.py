consumo_de_energia=float(input("consumo de energia kWh"))
conta_de_energia=consumo_de_energia*0.43+10
icms=conta_de_energia*(25/100)
valor_a_ser_pago=conta_de_energia+icms
print(round(valor_a_ser_pago,2))