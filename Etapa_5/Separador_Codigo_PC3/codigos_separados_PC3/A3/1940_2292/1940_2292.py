aminoacido = input("nome do aminoacido: ").upper()
o = 15.9994
c = 12.011
n = 14.0067
s = 32.006
h = 1.0079
GLUTAMINA = ((c*5)+(h*8)+(n*1)+(o*4))
TREONINA = ((c*4)+(h*9)+(n*1)+(o*3))
if (aminoacido == "TREONINA"):
   print(round(TREONINA, 2))
else:
   print(round(GLUTAMINA, 2))

