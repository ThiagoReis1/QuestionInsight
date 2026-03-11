qd= float(input())
preço = 2.86

valor = (preço * qd ) + 50.00

icms = valor * 0.34

valortotal = valor + icms

print (round(valortotal,2))
