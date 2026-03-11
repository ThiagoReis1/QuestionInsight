from numpy import*

alv = array(eval(input()))

i = 0
mp=0

while i<size(alv):
	if alv[i]==1:
		mp +=100
	elif alv[i] == 2:
		mp +=60
	elif alv[i] == 3:
		mp += 20
	else:
		mp += 0
	i+=1	
print(round(mp ,2))