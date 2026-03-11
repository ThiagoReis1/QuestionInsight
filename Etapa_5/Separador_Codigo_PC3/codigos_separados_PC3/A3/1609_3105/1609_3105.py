from numpy import*
danos=array(eval(input()))
busca=input("").upper().replace("R","L")
i=0
p=0
o=-1
while (i<size(danos)):
	if (busca==danos[i]):
		p=i
		o=1
	i=i+1
if (o==-1):
	print("NAO ENCONTRADA")
else:
	print(p)
		
		




