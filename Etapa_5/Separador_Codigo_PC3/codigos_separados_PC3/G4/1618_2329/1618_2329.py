from numpy import *
vet = array(eval(input("vet:")))
i = 1
while(i < size(vet)):
	print(vet[0],"x^",(size(vet)-i))