from numpy import*
i = 0
x = 0
anel = array(eval(input()))
while(anel[i] != 4):
	i = i + 1	
	if (anel[i] == 0):
		x = x + 80
	elif (anel[i] == 1):
		x = x + 40
	elif(anel[i] == 2):
		x = x + 20
	elif(anel[i] == 3):
		x = x + 10
	
print(x)



