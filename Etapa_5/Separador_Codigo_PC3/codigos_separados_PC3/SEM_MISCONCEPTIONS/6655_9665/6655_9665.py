from numpy import *

Vn = eval(input("digite a nota: "))

p = [5,1]
i = 0

while i < size(Vn):  

Mp = (Vn[1] * p[1]) + (Vn[2] * p[2]) + (Vn[3] * p[3]) + (Vn[4] * p[4]) + (Vn[5] * p[5]) / sum(p)
			  
print(round(Mp,2))