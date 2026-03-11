min_excedentes_mes = float(input("Quantos minutos excedentes consumidos no mês?"))
custo_plano_celular_mes = 45
custo_min_excedente = 0.97 * min_excedentes_mes
total_parcial = (custo_plano_celular_mes + custo_min_excedente)
imposto_valor = total_parcial * 0.42 
valor_final = imposto_valor + total_parcial
print(round(valor_final, 2))