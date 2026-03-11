from numpy import *
atv = array(eval(input("atividade:")))
gas = array(eval(input("gasto calorico:")))

i = 0
cal = zeros(size(atv))
while(i < size(atv)):
	if(atv[i] == "ALONGAMENTO"):
		cal[i] = 3*gas[i]
		i = i + 1
	elif(atv[i] == "CORRIDA"):
		cal[i] = gas[i]*10.3
		i = i + 1
	elif(atv[i] == "DANCA"):
		cal[i] = gas[i]*6.7
		i = i + 1
	elif(atv[i] == "ESCALADA"):
		cal[i] = gas[i]*9.7
		i = i + 1
	elif(atv[i] == "HIDROGINASTICA"):
		cal[i] = gas[i]*5
		i = i + 1
print(round(sum(cal),2))		