preco=0.43
fixo=10.00
kwh=float(input("insira a quantidade:"))
consumo=(kwh*0.43)
t=(consumo +fixo)
icms=t * (25/100)
total=t+icms
print(round(total  ,2))
