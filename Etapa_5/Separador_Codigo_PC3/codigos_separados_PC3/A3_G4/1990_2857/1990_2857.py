x = input("digite o nome do aminoacido: ")
o = 15.9994
c = 12.011
n = 14.0067
h = 1.00794
peso = 0
if(x == "GLUTAMINA".upper()):
   peso = (c*5) + (h*8) + (n*1) + (o*4)
   print(round(peso, 2))
elif(x == "SERINA".upper()):
   peso = (c*3) + (h*7) + n + (o*3)
   print(round(peso, 2))
elif(x == "TREONINA".upper()):
   peso = (c*4) + (h*9) + n + (o*3)
   print(round(peso, 2))
else:
   print("Entrada: ", x)
   print("Dado Invalido")
 
 