from math import *

mes = float(input("consumo mes: ")) #kWh
conta = (mes * 0.43 + 10)
icms = conta * 0.25
total = conta + icms
print(round(total, 2))