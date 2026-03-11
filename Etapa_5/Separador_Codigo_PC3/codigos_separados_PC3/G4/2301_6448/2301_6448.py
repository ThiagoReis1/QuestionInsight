from math import * 
lb= float(input("Lado b: "))
lc= float(input("Lado c: "))
ang = radians(float(input("Valor do angulo entre b e c: "))) 
a = sqrt( pow(lb,2) + pow(lc,2) - 2*lb*lc * cos(ang))
print(round(a,2))