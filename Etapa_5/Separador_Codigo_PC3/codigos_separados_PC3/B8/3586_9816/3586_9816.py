from numpy import*
acertos = array(eval(input("Digite os aneis de acerto:")))

i=0
acumuladora=0

while i< size(acertos):
	if acertos[i]==1:
		acumuladora+=100
	elif acertos[i]==2:
		acumuladora+=60
	elif acertos[i]==3:
		acumuladora+=+20
	elif acertos[i]==4:
		acumuladora==acumuladora
	i+=1
print(acumuladora)
