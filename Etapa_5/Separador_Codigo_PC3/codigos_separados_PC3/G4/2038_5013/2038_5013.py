s = input("Voce gostou do atendimento? (SIM/NAO): ").upper()
n = 0 #variavel contadora

#CALCULOS
while(s != 'S'):
	if(s == "SIM"):
		n = n + 1
	else:
		n = n + 0
	s = input("Voce gostou do atendimento? (SIM/NAO): ").upper()

#SAIDAS
print(n)

