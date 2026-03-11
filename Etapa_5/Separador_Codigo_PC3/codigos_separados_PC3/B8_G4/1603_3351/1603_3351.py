from numpy import*
v = array(eval(input("Mande as jogadas ae meu chegado: ")))
i = 0
c = 0
while(v[i] != 4):
	if(v[i] == 1):
		i = i + 1
		c = c + 80
	elif(v[i] == 2):
		i = i + 1
		c = c + 40
	elif(v[i] == 3):	
		i = i + 1
		c = c + 20
print(c)	