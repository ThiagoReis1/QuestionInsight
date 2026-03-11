cab= input("cabeça Aameul ou Hethradiah?")
d1= int(input("valor do dado 1: "))
d2= int(input("valor do dado 2: "))
d3= int(input("valor do dado 3: "))

if cab== "Aameul" :
	
	dano= 8 + (d1+d2+d3) 
	print(dano)
	
else:
	
	dano=2*(d1+d2+d3)
	print(dano)