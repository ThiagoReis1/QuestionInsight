import math

r = float(input("Raio : "))
n = int(input("Numero de lados :"))

var1 = (r* math.cos(math.pi/n))**2 
var2 = math.tan(math.pi/n)


print(round(1/2 * var1 *var2, 2))