aminoacido = input("nome do aminoacido: ")
aminoacido = aminoacido.lower()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
if aminoacido=="histidina":
   print(round((C*6+H*10+N*3+O*2),2))

if aminoacido=="prolina":
   print(round((C*5+H*10+N+O*2),2))