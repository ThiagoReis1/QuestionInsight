from numpy import*
nome = array(eval(input()))
minuto = array(eval(input()))

i = 0;
cont0 = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
while(i<size(nome)):
	if(nome[i] == "ALONGAMENTO"):
	   cont1 = cont1 + (minuto[i]*3.0)
	elif(nome[i] == "CORRIDA"):
	   cont0 = cont0 + (minuto[i]*10.3)
	elif(nome[i] == "DANCA"):
	   cont2 = cont2 + (minuto[i]*6.7)
	elif(nome[i] == "ESCALADA"):
	   cont3 = cont3 + (minuto[i]*9.7)
	elif(nome[i] == "HIDROGINASTICA"):
	   cont4 = cont4 + (minuto[i]*5.0)	
	i =i + 1
total = cont0 + cont1 + cont2 + cont3 + cont4
print(round(total, 2))