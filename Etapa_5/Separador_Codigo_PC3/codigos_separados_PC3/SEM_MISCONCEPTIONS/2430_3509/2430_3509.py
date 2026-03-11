from math import*
capital = float(input("valor total da compra"))
tempo = int(input("quantidade das parcelas ao mes"))
txjuros = 3

juros = (capital*txjuros*tempo)/100
m = (capital+juros)
print(round(m,2))









