x=input("x?")
t=0

while(x.upper()!="S"):
	if(x.upper()=="A"):
		t=t+1
	else:
		t=t
	x=input("x?")
print(t)