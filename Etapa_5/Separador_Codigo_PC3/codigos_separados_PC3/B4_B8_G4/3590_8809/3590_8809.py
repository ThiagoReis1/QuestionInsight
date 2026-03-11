from numpy import*
d=eval(input("valor tirado no dado: "))
f=len(d)
i=0
t=0
while i < f:
	h=d[i]
	if h == 1:
		t=t+10
	elif h == 2:
		t=t+5
	elif h == 3:
		t=t+0
	elif h == 4:
		t=t+5
	elif h == 5:
		t=t+20
	elif h == 6:
		t=t+10
	i=i+1
print(t)		