aminoacido = input("nome do aminoacido:").upper()
#Dados
o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
ARGININA = ((c*6)+(h*15)+(o*2)+(n*4))
TIROSINA = ((c*9)+(h*11)+n+(o*3))

if (aminoacido == "ARGININA"):
  	print(round(ARGININA,2))
else:
  	print(round(TIROSINA,2))