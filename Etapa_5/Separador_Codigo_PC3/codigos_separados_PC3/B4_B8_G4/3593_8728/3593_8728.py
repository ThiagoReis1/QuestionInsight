from numpy import*
x = array(eval(input()))
t = 200
for i in range(len(x)):
	if x[i]==1:
		t=t/2
	elif x[i]==2:
		t=t*3
	elif x[i]==3:
		t=t/2
	elif x[i]==4:
		t=t*3
	elif x[i]==5:
		t=t/2
	elif x[i]==6:
		t=t*3
print(round(t,2))