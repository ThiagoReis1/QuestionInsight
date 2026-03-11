from math import *

qtde_min = float(input("Digite a quantidade de minutos excedentes: "))

custo = (((qtde_min * 0.97) + 45))
icms = (custo * 42) /100
valor_total = custo + icms			

print (round(valor_total,2))
			