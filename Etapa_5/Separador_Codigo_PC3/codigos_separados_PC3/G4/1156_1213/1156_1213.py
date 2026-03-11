nicc = float(input("Numero inicial de celulas cancerosas:"))
tpr = float(input("Taxa percentual de reducao:"))
#tpr1 = tpr / 100
nncc = float(input("Numero de novas celulas cancerosas:"))
q = 1
tncc = nicc
tncc1 = 0
while (tncc1 <= 500000):
	tncc1 = tncc - (tncc*tpr)
	tncc1 = tncc1 + nncc
	tncc = tncc1
	q = q+1
print(q)	
	
