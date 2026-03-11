from numpy import*

saques=array(eval(input("insira os saques: ")))
cont=0

for i range(size(saques)):
	if saques[i]>=2000:
	cont += 1