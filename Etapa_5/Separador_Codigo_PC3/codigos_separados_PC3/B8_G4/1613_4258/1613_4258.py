from numpy import *

nomes = array(eval(input("Nomes de atividades: ")))
dur = array(eval(input("DUracoes em minutos das atividades: ")))

i = 0
cal = 0

while(i < (size(nomes) and size(dur))):
	if(nomes[i] == "ALONGAMENTO"):
		cal = cal + dur[i]*3
	elif(nomes[i] == "CORRIDA"):
		cal = cal + dur[i]*10.3
	elif(nomes[i] == "DANCA"):
		cal = cal + dur[i]*6.7
	elif(nomes[i] == "ESCALADA"):
		cal = cal + dur[i]*9.7
	elif(nomes[i] == "HIDROGINASTICA"):
		cal = cal + dur[i]*5
		
	i = i + 1
	
print(round(cal, 2))