import math

var1= math.radians(float(input("a")))
var2= float(input("b"))
g= 9.8
d= var2**2*math.sin(2*var1)/g
print(round(d,2))