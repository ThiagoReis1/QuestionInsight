aminoacido = input("nome do aminoacido?: ")
c = 12.011
o = 15.9994
n = 14.0067
e = 32.066
h = 1.0079
fenilalanina = (c*9+h*11+o*2+e)
tirosina = (c*9+h*11+n+o*3)
if (aminoacido == "fenilalanina"):
   print(round(fenilalanina, 2))
else:
   print(round(tirosina, 2))