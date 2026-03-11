from math import*
valor = float(input("produto   :"))
frete=(valor/100)*5
desconto=(valor/100)*40
precodesconto=valor-desconto
real=precodesconto-valor
print(round(precodesconto,2))
print(round(frete,2))