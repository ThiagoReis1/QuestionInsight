from numpy import*

b= input("digite o nipe da carta: ").upper().split(",")
i=0
cont = zeros(4,dtype=int)
for i in range(len(b)):
	if b[i]=="C":
		cont[0]=cont[0]+1
	elif b[i]=="O":
		cont[1]=cont[1]+1
	elif b[i]=="P":
		cont[2]=cont[2]+1
	elif b[i]=="E":
		cont[3]=cont[3]+1
print(cont)
		