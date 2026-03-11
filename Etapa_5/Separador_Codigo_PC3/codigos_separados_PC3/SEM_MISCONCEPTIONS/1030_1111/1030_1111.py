minutos_excedente = float(input("Quantos minutos excendente?"))
custo = 45.00
excedente = 0.97
porcentagem = 42/100
custo_t = custo + excedente * minutos_excedente
custo_total= custo_t * porcentagem
gasto = custo_t + custo_total
print (round(gasto, 2))