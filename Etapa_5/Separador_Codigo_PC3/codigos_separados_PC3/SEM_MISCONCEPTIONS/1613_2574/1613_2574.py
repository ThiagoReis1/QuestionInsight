from numpy import*

atividade = array(eval(input("Insira as atividade fisicas: ").upper()))
tempo = array(eval(input("Insira o tempo de cada atividade: ")))

i = 0
a = 0
while(i < size(atividade)):
	if(atividade[i] == "ALONGAMENTO"):
		a = a + tempo[i]*3	
	elif(atividade[i] == "CORRIDA"):
		a = a +tempo[i]
	else:
		e = 9.7*tempo[i]
	i = i + 1
total = a + c + e

print(round(total,2))
		
		
	
	
	

