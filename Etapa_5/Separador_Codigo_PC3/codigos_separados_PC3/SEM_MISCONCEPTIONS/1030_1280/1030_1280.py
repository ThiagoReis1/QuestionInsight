x = float(input("digite a quantidadde de minutos gastos: "))

custo_plano = 45.0
ex= x * 0.97
imposto = (custo_plano + ex)*42/100
total = imposto + custo_plano + ex
print(round(total,2))