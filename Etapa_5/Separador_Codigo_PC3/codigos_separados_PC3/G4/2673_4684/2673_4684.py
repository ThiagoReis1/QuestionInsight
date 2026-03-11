var1 = float(input("Qual o valor do raio? "))
var2 = int(input("Qual o numero de lados? "))

import math
cal = 2*(var1)*(math.sin(math.pi/var2))

print(round(cal,2))