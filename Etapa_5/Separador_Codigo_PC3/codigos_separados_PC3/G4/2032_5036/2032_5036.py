face = int(input("face do dado:"))
cont = 0
while face != -1:
	if face == 5:
		cont = cont + 1
		
	face = int(input("face do dado:"))
	
print(cont)