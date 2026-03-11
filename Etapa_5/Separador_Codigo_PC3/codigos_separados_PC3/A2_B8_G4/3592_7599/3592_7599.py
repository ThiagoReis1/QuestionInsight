from numpy import *
d = array(eval(input("dados:")))
i = 100
j = 0
while(j<size(d)):
	if(d[j]==1):
		i = i 
	elif(d[j]==2):
		i = i * 2
	elif(d[j]==3):
		i = i/3
	elif(d[j]==4):
		i = i * 4
	elif(d[j]==5):
		i = i/5
	elif(d[j]==6):
		i = i * 6
	j = j + 1
print(round(i,2))
		