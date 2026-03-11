from numpy import*

j= array(eval(input()))
pon= 10000

i=0

while(i < size(j)):
	jogada = j[i]
	if(jogada == 1):
		pon = pon * 2
	elif(jogada == 3):
		pon = pon / 2
	elif(jogada == 4):
		pon = pon / 4
	i+=1
print(round(pon,2))