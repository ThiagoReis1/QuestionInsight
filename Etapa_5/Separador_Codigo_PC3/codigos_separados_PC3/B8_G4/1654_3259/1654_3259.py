from numpy import *
cid = input("Estados: ")
a=0
b=0
c=0
d=0
e=0
new = cid.split(",")
saida = zeros(5, dtype=int)
for i in range(size(new)):
	if (new[i]=="AM"):
		a = a + 1
	elif (new[i] =="PE"):
		b = b + 1
	elif (new[i] =="MG"):
		c = c + 1
	elif (new[i] =="SP"):
		d = d + 1
	elif (new[i] =="RS"):
		e = e + 1
saida[0]=a
saida[1]=b
saida[2]=c
saida[3]=d
saida[4]=e
print(max(saida))
print(saida)