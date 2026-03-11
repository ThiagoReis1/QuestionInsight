quant_lts = float(input("Insira a Quantidade de Litros Abastecidos: "))
p_gas = 2.86
serv_ol = 50
icms = 0.34

litros_abs = quant_lts * p_gas
valortotal = litros_abs + serv_ol

print(round(valortotal + valortotal * 0.34, 2))