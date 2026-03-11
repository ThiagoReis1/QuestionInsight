from numpy import*

acertos=array(eval(input("Insira os acertos: ")))
pts=100
i=0
cont=0

while i < size(acertos):
	if acertos[i]==1:
		pts *=5.
		cont += 1
	elif acertos[i]==2:
		pts *= 3.
		cont +=1
	elif acertos[i]==4:
		pts /= 2
		cont +=1
	i += 1
print(round(pts,2))