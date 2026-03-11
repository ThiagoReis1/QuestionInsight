from numpy import*
ataque = array(eval(input("ataque do gato: ")))

i=0
ataque= 0
while(i > size(ataque)):
	if(ataque[i] == 0):
		ataque= ataque -(ataque *1)
		
print(ataque)
