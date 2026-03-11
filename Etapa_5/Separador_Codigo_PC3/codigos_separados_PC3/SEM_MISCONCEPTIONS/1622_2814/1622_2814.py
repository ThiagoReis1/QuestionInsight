from numpy import*
passageiros_entraram = array(eval(input("passageiros que entraram:")))
passageiros_sairam = array(eval(input("passageiros que sairam:")))

i = 0;
cont = 0;
while(i<size(passageiros_entraram)):
	cont += passageiros_entraram[i];
	cont -= passageiros_sairam[i];
	i += 1;
	
print(cont)