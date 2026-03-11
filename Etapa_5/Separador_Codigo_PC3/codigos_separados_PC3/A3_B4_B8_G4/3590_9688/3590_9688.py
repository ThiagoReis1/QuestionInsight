from numpy import *
num = array(eval(input("Insira a jogada: ")))
x = [1,2,3,4,5,6]
i = 0 
t = size(num) - 1
j1 = 0
while i <= t:
	if num[i] == 1:
	   j1 = j1+10
	elif num[i] == 2:
		j1 = j1+5
	elif num[i] == 3:
		j1 = j1+0
	elif num[i] == 4:
		j1 = j1+5
	elif num[i] == 5:
		j1 = j1+20
	elif num[i] == 6:
		j1 = j1+10
	
	i+=1
	
print(round(j1,1))