custo_plano = 45.00
custo_por_minuto = 0.97

minutos_excedentes = int(input("Digite a quantidade de minutos excedentes consumidos: "))

valor_minutos_excedentes = minutos_excedentes * custo_por_minuto

aumento_cms = 0.42 
valor_aumentado = valor_minutos_excedentes * (valor_minutos_excedentes + aumento_cms)

valor_total = custo_plano + valor_aumentado

valor_total = round(valor_total, 2)
print("O valor a ser pago R$", (valor_total))