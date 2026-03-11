s= (input())
i=0
total=0
m=0
p=0
r=0
for produto in s:
	if produto == "M":
		total+= 7.25
		m+=1
	elif produto == "P":
		total+= 4.75
		p+=1
	elif produto == "R":
		total+= 3.50
		r+=1
	i+=1
print(round(total,2),m,p,r)		
	