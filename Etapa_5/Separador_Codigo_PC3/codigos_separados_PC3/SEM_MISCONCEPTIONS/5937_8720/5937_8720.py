lit=float(input("Litros abastecidos:"))
gas=2.86*lit
toleo=50
icms=(34/100)*(gas+toleo)
total=gas+toleo+icms
print(round(total, 2))