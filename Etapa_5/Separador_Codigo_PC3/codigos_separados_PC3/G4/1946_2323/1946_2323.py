aminoacido = input("nome do aminoacido: ")
aminoacido = aminoacido.lower()
O = 15.999
C = 12.011
N = 14.0067
S = 32.066
H = 1.0079
if aminoacido =="fenilalanina":
   print(round(C*9+H*11+O*2+S,2))
if aminoacido =="tirosina":
   print(round(C*9+H*11+N+O*3,2))