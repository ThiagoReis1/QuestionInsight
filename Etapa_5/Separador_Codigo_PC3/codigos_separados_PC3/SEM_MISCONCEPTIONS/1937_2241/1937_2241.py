aminoacido = input("nome do aminoacido? ")
c = 12.011
o = 15.9994
n = 14.00674
h = 1.00794

alanina = ((c*3) + (h*7) + n + (o*2))
valina = ((c*5) + (h*11) + n + (o*2))

if (aminoacido.upper() == "ALANINA"):
  print(round(alanina, 2))
else:
  print(round(valina, 2))
