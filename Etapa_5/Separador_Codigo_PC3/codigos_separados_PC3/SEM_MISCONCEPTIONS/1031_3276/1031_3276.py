a =float(input("Litros abastecidos:"))
gasolina =2.86
troca_oleo =50
icms =34/100
gasto_gasolina =a*gasolina
gasolina_oleo = gasto_gasolina + troca_oleo
valor = gasolina_oleo*icms + gasolina_oleo
print(round(valor,2))