# Entrada de informacoes
nome = input("aminoacido:")
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
asparagina = ((c*4) + (h*8) + (n*2) + (o*3))
glutamina = ((c*5) + (h*8) + (n*1) + (o*4))
triptofano = ((c*11) + (h*11) + (n*2) + (o*2))

if(nome=="asparagina"):
  print(round(asparagina,2))
elif(nome=="glutamina"):
  print(round(triptofano,2))

else:
  print("Entrada:", nome)
  print("Dado Invalido")
	
