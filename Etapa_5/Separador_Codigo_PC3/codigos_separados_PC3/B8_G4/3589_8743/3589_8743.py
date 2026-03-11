from numpy import*
a = array(eval(input("Digite aqui: ")))
p = 0
i = 0
while(i < size(a)):
	if(a[i] == 1):
		p = p + 80
		
	elif(a[i] == 2):
		p = p + 40
		
	elif(a[i] == 3):
		p = p + 20
	
	elif(a[i] == 4):
		p = p + 10
	i = 1 + i
print(p)