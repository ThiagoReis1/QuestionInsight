from numpy import*
vet= input()
v1 = vet.upper()
c=0
while(c <(vet)):
	if(v1[c]=="R"):
		v2=vet[c].replace("R","L")
		print(v2)
		print(c)
c = c+1
	