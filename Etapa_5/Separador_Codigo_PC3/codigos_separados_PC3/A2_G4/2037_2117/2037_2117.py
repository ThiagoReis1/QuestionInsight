i=int(input("idade: "))
m=0

while(i!=-1):
	if(i<18):
		m=m+1
	else:
		m=m
	i=int(input("idade: "))
print(m)