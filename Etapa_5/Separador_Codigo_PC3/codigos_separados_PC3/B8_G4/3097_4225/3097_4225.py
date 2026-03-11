p = int(input( ))
t = 0
while(p!=0):
	if(p==1):
		t = t+25
	elif(p==2):
		t = t+18
	elif(p==3):
		t = t+12
	elif(p>=4)and(p<=10):
		t = t+(14-p)
	elif(p>10):
		t = t+0
	p = int(input( ))
print(t)