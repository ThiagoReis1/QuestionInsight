from numpy import *
anel = array(eval(input("Quais aneis acertados pelo jogador: ")))

pont = 10000
i = 0

while i < size(anel):
	if (anel) [i] == 1:
		pont = pont * 2
	if (anel) [i] == 3:
		pont = pont /2
	if (anel) [i] == 4:
		pont = pont /4
	i = i + 1
	
print(round(pont, 2))	