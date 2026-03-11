ataque= input("Espada ou Cauda? ").lower()

if(ataque=='espada'):
	D1= int(input("Face do dado: "))
	D2= int(input("Face do dado: "))
	D3= int(input("Face do dado: "))
	D4= int(input("Face do dado: "))
	de= (D1+6)+(D2+6)+(D3+6)+(D4+6)
	print(de)
	
else:
	D1= int(input("Face do dado: "))
	D2= int(input("Face do dado: "))
	D3= int(input("Face do dado: "))
	D4= int(input("Face do dado: "))
	dc= (D1+D2+D3)*D4
	print(dc)