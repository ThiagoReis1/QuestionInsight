#-------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS 
# ANA REBECA CAVALCANTE EVANGELISTA 
# MATRICULA: 21456290
# DATA: 28/07/2016
# OBJETIVO: População lambaris e tucunarés.
#-------------------------------------------

from math import *

pop_lbr = int(input("População inicial de lambaris: "))
pop_tcr = int(input("População inicial de tucunares: "))
tx_lbr = float(input("Taxa de crescimento lambaris: "))
tx_tcr = float(input("Taxa de crescimento tucunares: "))

i = 1

while (pop_lbr > pop_tcr):
	
	cresc_lbr = pop_lbr * tx_lbr
	pop_lbr = pop_lbr + cresc_lbr - (pop_tcr * 2)
	cresc_tcr = pop_tcr * tx_tcr
	pop_tcr = pop_tcr + cresc_tcr
	i = i + 1

print (i)