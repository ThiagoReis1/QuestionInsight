i = int(input("informe a idade: "))
cont = 0
mi = 0
f = 0
while (i!= -1):
	if (i<18):
		cont = cont + 1 
	elif (i>=18):
		mi = mi + 1 
		
	i = int(input("informe a proxima idade: "))
		
t = cont + mi	
f = (cont*100)/(t)
	 
print (t)
print(round(f,2))