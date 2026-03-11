custo_mes = 45
minuto_excedente = float(input("minutos excedentes: "))
custo_min = minuto_excedente * 0.97

semi_total = custo_mes + custo_min

imposto = semi_total * 0.42

total = semi_total + imposto
print(round(total,2))