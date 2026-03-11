x=int(input("valor x:"))
y=int(input("valor y:"))
soma=0
while(x<y+1):
	if(x%7==0):
		soma=soma+x
	x=x+1
print(soma)