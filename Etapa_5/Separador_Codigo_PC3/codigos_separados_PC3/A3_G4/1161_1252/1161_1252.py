#Patrick Chessmam	- 21200931

Z = int(input("Digite numero de zumbis: "))
H = int(input("Digite numero de habitantes: "))
X = int(input("Digite capacidade de transformar p em z: "))		  
Y = int(input("Digite capacidade de exterminar zumbi: "))	
		  
#Acumuladora
zumbis = Z
#contadora
dias = 0		  

while (H < Z) :
	(Z * X) - (H * Y)	  
	zumbis = Z * dias
	dias = dias + 1
	print (dias)
	
		  