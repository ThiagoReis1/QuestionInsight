consumo = float(input("consumo total:")) * 0.28
valfix = 23.00
conmin = consumo + valfix
RF = conmin * 31/100
valorpag= conmin + RF
print(round(valorpag, 2))