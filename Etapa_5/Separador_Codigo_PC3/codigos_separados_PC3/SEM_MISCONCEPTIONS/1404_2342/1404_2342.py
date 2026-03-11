ataque = input("coloque um ataque: aameul/hethrediah")
nome1 = "AAMEUL"
nome2 = "HETHREDIAH"
d1 = int(input("numero do dado: "))
d2 = int(input("numero do dado: "))
d3 = int(input("numero do dado: "))

if(ataque.upper() == nome1):
	print(d1 + d2 + d3 + 8)
if(ataque.upper() == nome2):
   print(2 * d1 + d2 + d3)





