i = int(input())
c = int(input())
d = int(input())
cont = 0
aux = 0
b=0
while(b < 200):
	aux = aux + (c*cont) - (d*cont)
	b = i + aux
	cont = cont + 1
	
print(b)
print(cont)
