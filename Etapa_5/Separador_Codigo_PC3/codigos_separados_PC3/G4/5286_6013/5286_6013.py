n = int(input()) 
cont = 0
c =0


while (n!=0):
	cont = cont + 1
	if(n%2==0):
		c = c + 1
	b = (100/cont)*c
	n = int(input())	
	
print(cont)
print(round(b,2))