nome = input("aminoacido:")
o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794
aspartato = ((c*4) + (h*6) + (n*1) + (o*4))
fenilalanina = ((c*9)+(h*11)+(o*2)+(s))
tirosina = ((c*9)+(h*11)+(n)+(o*3))
if(nome=="aspartato"):
  print(round(aspartato,2))
elif(nome=="fenilalanina"):
  print(round(fenilalanina,2))
elif(nome=="tirosina"):
  print(round(tirosina,2))
else:
  print("Entrada:",nome)
  print("Dado Invalido")