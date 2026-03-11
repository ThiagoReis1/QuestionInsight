from numpy import*

valor = array(eval(input()))
i = 0
des = 0

while(i<size(valor)):
	if(valor[i]>=80):
		des = des + 5
	i = i + 1
pt = sum(valor)-des
print(round(pt,2))