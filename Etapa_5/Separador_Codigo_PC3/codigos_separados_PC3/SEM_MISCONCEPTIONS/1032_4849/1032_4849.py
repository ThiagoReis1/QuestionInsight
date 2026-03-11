from math import*

valor = float(input("Qual o valor da encomenda: "))
tx = 12

imposto=(valor/100)*81

vt = imposto+valor+tx

print(round(vt,2))

