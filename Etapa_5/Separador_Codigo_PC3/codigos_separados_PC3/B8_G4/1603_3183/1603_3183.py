from numpy import*
a = array(eval(input("aneis acertados pelo jogador ")))
p = 0
i = 0
while(a[i] < 4):
	if(a[i] == 1):
		p = p + 80
	elif(a[i] == 2):
		p = p + 40
	elif(a[i] == 3):
		p = p + 20
	i = i + 1
print(p)