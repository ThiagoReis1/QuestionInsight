gasto=float(input('Minutos excedentes:'))
valor=45
juros=0.97
icms=42
pg=(valor/100*icms)*juros
print(round(pg, 2))