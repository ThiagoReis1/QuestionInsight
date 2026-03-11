from numpy import*

numeros_aneis_1 = array(eval(input("Digite os aneis do primeiro jogador :")))
numeros_aneis_2 = array(eval(input("Digite os aneis do segundo jogador :")))

i = 0;
anel_1 = 40
anel_2 = 20;
anel_3 = 10;
anel_4 = 0;

while(i < size(numeros_aneis_1) and i < size(numero_aneis_2)): 
	if(numeros_aneis_1[i] and numeros_aneis_2[i]  == 1): 
		anel_1 += 1;
		i += 1;
		
jogador_1 = anel_1 + anel_2 + anel_3 + anel_4
jogador_2 = anel_1 + anel_2 + anel_3 + anel_4

if(jogador_1 < jogador_2): 
   print("JOGADOR DOIS")
elif(jogador > jogador_2): 
   print("JOGADOR UM")
elif(jogador_1 == jogador_2): 
   print("EMPATE")