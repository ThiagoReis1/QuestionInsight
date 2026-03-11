from numpy import *
alvos =array(eval(input()))
i=0
t=0
while i < size(alvos):
	if alvos [i]== 1:
		t=t+80
	if alvos [i]== 2:
		t=t+40
	if alvos [i]== 3:
		t=t+20
	if alvos [i]== 4:
		t=t+10
	i=i+1
print(t)