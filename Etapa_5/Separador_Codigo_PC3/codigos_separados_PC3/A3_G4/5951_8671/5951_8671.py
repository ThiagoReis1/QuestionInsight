var1 = input("voce quer T ou S: ")
qtde = int(input("qtde de T ou S: "))
a = int(input("qtde de acai: "))

tapioca = "T"
salgado = "S"

if (var1 == "S"):
   S = (qtde * 5.00) + (a * 12.00) 
   print(S)
else:
   T = (qtde * 4.50) + (a * 12.00)
   print(T)
