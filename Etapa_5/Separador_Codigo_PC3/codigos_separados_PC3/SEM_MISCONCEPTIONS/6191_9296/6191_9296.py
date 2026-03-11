from numpy import*

face = input("Digite a face da moeda. ").upper()

cont = 0
while(face == 'CARA'):
	cont = cont + 1
	print(face)
elif(face == 'S'):
	print(cont)
	