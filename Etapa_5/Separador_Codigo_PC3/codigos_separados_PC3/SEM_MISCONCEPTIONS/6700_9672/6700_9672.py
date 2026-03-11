numero_dias= int(input("Insira o numero de dias: "))
valor_aluguel= 50 * numero_dias
valor_manutencao= 30
icms= 0.18 
valor_icms= (valor_aluguel + 30) * icms

total_gasto=  valor_aluguel + valor_manutencao + valor_icms

print(round(total_gasto, 2))