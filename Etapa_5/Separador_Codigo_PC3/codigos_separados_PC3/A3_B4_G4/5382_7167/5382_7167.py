from numpy import*
x=input().upper()
i=0
t=0
while i<len(x):
	if x[i]=="A":
		t=t+0.25
	elif x[i]=="E":
		t=t+0.25
	elif x[i]=="I":
		t=t=0.25
	elif x[i]=="O":
		t=t+0.25
	elif x[i]=="U":
		t=t+0.25
	else:
		t=t+0.27
	i=i+1
print(round(t, 2))	