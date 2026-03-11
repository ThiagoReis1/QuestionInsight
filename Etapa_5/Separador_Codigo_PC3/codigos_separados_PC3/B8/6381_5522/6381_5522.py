from numpy import*
cartas = input().upper().split(",")
x=zeros(4,dtype=int)
for i in range(len(cartas)):
	if cartas[i] == "C":
		x[0]+=1
	elif cartas[i] == "O":
		x[1]+=1
	elif cartas[i] == "P":
		x[2]+=1
	elif cartas[i] == "E":
		x[3]+=1
print(x)
