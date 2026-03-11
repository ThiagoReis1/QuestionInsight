from numpy import*
j = array(eval(input("qual os acertos do jogador?")))
i=0
pont = 0
while(i<len(j)):
	if(j[i] == 1):
		pont=pont+80
	elif(j[i] == 2):
		pont = pont+40
	elif(j[i] == 3):
		pont= pont+20
	elif(j[i] == 4):
		pont=pont+10
	i=i+1
print(pont)
idalinasantos3007@gmail.com