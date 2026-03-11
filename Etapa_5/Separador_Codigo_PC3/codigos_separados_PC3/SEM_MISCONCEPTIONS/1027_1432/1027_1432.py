# Universidade Federal do Amazonas
# Aluno: Eules Leonardo S Lima
# Ex 02 - Calcular valor a ser pago na conta de energia
from math import *
vl_kwh = 0.43
taxa_iluminacao = 10.0
percentual_icms = 0.25
consumo = float(input("Qual o consumo de em KWh: "))
valor_a_pagar = (taxa_iluminacao + (consumo * vl_kwh)) * (1 + percentual_icms)
print(round(valor_a_pagar,2))                 
