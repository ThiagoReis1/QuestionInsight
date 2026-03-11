# Pedro Afonso
# Avaliação 1 ICC

from math import *

valor_pago = float(input("digite o valor= "))

#custo da conta de agua

custo_agua = (0.37 * 26 + 15)- 0.032 

#ICMS

icms = 0.35

volume = (custo_agua / icms) 

print(round (volume, 2))





