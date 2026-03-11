n = int(input("numero:  "))

a = 0
p = 0
while n !=0:
	p = p+1
	if n >=1:
		if n %2==0:
			a = a+1
	n = int(input())
			
	
print(p)
print(round(a*100/p, 2))

			
			
	