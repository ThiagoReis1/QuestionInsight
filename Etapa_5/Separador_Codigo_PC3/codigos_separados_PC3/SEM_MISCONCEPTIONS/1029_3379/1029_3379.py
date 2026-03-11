minutos= float(input("Minutos de chamada "))
consumo_parcial= float((minutos * 0.28)+23.00)
consumo= (consumo_parcial/100) * 31 + consumo_parcial

print(round(consumo,2))