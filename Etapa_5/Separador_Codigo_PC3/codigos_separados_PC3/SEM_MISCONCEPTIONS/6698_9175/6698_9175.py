quantidade_de_pracas = float (input("Digite a quantidade de pracas: "))
valor_total_a_ser_pago = quantidade_de_pracas * 9.80 + 20 
valor_total = valor_total_a_ser_pago + valor_total_a_ser_pago * 0.15
print(round(valor_total, 2))
										
										