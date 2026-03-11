face = int(input("Informe o valor da face do dado: "))

c = 0

while(face != -1 and face <= 10):
	face = int(input("Informe o valor da face do dado: "))
	if(face == 5):
		c = c + 1
print(c)