massa = (float(input("massa:")))
from math import *
quant_flaw = 2**(1 + massa/1000)
quant_soul = massa * pi**2/3141
quant_oleo = 2 * sqrt(massa/40)
print(round(quant_flaw,2))
print(round(quant_soul,2))	
print(round(quant_oleo,2))