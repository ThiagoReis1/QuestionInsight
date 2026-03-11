from math import*

preco = float(input("valor sem desconto: "))
cod = int(input("insira cod: "))

valor_final = round((preco - (preco*(0.4))),2)
print(valor_final)
 
if (cod == 1):
   print((preco*(10/100))
  elif (cod == 2):
	print(preco*(8/100))
  elif (cod == 3):
	print(preco*(1))
  elif (cod == 4):
	print(preco*(2/100))
else:
	print("Nada")