from math import *
volume= float(input())
fixo= 15.0

pago= (volume * 0.37) + fixo
pago1= (pago * 35)/100
pago3= pago + pago1
print(float(round(pago3,2)))
