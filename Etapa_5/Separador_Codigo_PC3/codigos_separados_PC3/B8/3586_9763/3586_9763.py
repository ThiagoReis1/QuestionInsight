from numpy import*

ac = array(eval(input("Informe os alvos acertados")))
i = 0
acertos = 0
while i < size(ac): 
	if ac[i] == 1:
		acertos = acertos + 100
	elif ac[i] == 2:
		acertos = acertos + 60
	elif ac[i] == 3:
		acertos = acertos + 20
	elif ac[i] == 4:
		acertos = acertos + 0
	i = i + 1
	
print(acertos)