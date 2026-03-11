cor = input ("vermelho ou preta:").upper()
pretas = 0

while (cor != "S" ):
	
	if (cor =="PRETA"):
		pretas = pretas + 1
	cor = input ("vermelho ou preta:").upper()
print (pretas)
