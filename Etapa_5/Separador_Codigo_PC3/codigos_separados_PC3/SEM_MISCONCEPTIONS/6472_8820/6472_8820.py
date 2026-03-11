from math import *

# faça seu código aqui!

c_l = float(input("comprimento do lado: "))

apetema = (c_l)/ (2* tan(pi/9))

ae = (9 * c_l * apetema) / 2
					
print (round(ae,2))
