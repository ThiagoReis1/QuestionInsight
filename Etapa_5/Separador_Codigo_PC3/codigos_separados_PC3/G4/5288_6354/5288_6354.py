n = int(input("informe a idade: "))
c = 0
t = 0
while (n!= -1):
	if(n<18):
		c = c + 1
	t = t + 1
	n = int(input("informe a idade: "))
r = (c/t) * 100
print(t)
print(round(r,2))
		
 

	
	