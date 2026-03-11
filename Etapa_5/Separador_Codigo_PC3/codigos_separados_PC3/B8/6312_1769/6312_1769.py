from numpy import *

produtos = input()
total=0
i=0
biscoito=0
cereal=0
enlatado=0

while(i < len(produtos)):
	if(produtos[i]=="B"):
		total+= 3.75
		biscoito+= 1
	elif(produtos[i]=="C"):
		total+= 7.90
		cereal+= 1
	elif(produtos[i]=="E"):
		total+= 9.85
		enlatado+= 1
		
	i+= 1
	
print(round(total, 2), biscoito, cereal, enlatado)
