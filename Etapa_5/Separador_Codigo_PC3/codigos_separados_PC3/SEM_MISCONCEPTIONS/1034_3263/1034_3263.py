#CHILPERICO

dolar = float(3.55)

doze_reais = float(12.00)

reais = float(input("qual a quantia em reais: "))

taxa_fixa = reais - doze_reais

negocio = taxa_fixa / dolar

print(round(negocio, 2))