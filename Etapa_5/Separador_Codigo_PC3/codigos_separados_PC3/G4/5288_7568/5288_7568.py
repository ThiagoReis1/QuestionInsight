d = int(input("idade: "))
m = 0
i = 0

while(d!=-1):
	i = i + 1
	if(0<d<18):
		m = m+1
	d = int(input("idade: "))
j = (m/i)*100
print(i,(round(j,2)))
		
	