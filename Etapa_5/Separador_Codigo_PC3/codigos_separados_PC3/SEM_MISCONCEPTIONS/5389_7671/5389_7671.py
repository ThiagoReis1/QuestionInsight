#Senhas
from numpy import *
#vogais = array(["A", "E", "I", "O", "U"])

sen = input("Digite a senha: ")

i = 0
total = 0

#while(i<len(sen)):
#	if(sen[i] == )
#	i = i + 1














#while(i<len(sen)):
#if((sen[0].upper() == "A") or (sen[0].upper() == "E") or (sen[0].upper() == "I") or (sen[0].upper() == "O") or (sen[0].upper() == "U")):
#	total = total + 3.15
#	i = i + 1
while(i<len(sen)):
	if((sen[i].upper() == "A") or (sen[i].upper() == "E") or (sen[i].upper() == "I") or (sen[i].upper() == "O") or (sen[i].upper() == "U")):
		total = total + 3.15
	else:
		total = total + 4.17
	i = i + 1
	
print(round(total,2))















