preco= float(input("quantidade de ouro"))
arma= input("nome da arma: ")
dano=input("fator de sucesso")

if(preco==100):
   print("ESPADA")
   print(dano*10)	
elif(preco==30):
   print("MACHADO")
   print(dano + 3)
elif(preco==50):
   print("MARRETA")
   print(dano + 5)
elif(preco>10)	:
	print("Entrada invalida")

else:
	print("PO insuficiente")
	

   		 

