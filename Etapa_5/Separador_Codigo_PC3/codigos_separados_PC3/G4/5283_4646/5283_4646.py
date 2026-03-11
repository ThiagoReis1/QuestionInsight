x = int(input("numero"))
i = 0
cont = 0
while(x!=0):
	i=i+1
	if(x>0):
		cont=cont+1
	
	x = int(input())
print(i)
p = (cont/i)*100
print(round(p,2))