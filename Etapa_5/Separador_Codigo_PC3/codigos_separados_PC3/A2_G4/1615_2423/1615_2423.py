from numpy import*
v1 = array(eval(input("Quais os aneis acertados: ")))
v2 = array(eval(input("Quais os aneis acertados: ")))
i = 0
j = 0
while(i < size(v1)):
	if(v1[i] == 1):
		j = j + 40
	elif(v1[i] == 2):
		j = j + 20
	elif(v1[i] == 3):
		j = j + 10
	else:
		j = j
	i = i + 1
	
k = 0
l = 0
while(l < size(v2)):
	if(v2[l] == 1):
		k = k + 40
	elif(v2[l] == 2):
		k = k + 20
	elif(v2[l] == 3):
		k = k + 10
	else:
		k = k
	l = l + 1
if(j > k):
	print("JOGADOR UM")
elif(j < k):
	print("JOGADOR DOIS")
else:
	print("EMPATE")
		  	  
		  
		  