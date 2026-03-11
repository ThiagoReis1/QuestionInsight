from numpy import *
d = array(eval(input("dado: ")))
i = 0
pontos = float(100)
while(i<size(d)):
	if(d[i] ==1):
		pontos = pontos*1
	if(d[i] ==2):
		pontos = pontos*2
	if(d[i] ==3):
		pontos = pontos/3
	if(d[i] ==4):
		pontos = pontos*4
	if(d[i] ==5):
		pontos = pontos/5
	if(d[i] ==6):
		pontos = pontos*6
	i = i+1

print(round(pontos,2))