from numpy import*
face = array(eval(input("Valor do dado: ")))
i = 0
c = 0
while (i < size(face)):
	if (face[i] == 1):
		c += 10
	if (face[i] == 2):
		c += 5
	if (face[i] == 3):
		c += 0
	if (face[i] == 4):
		c += 5
	if (face[i] == 5):
		c += 20
	if (face[i] == 6):
		c += 10
	i = i + 1	
print(c)
	
	