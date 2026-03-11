a = input("face:").lower()

t=0 

while(a != "s"):
	if(a == "cara"):
		t = t + 1
	if(a =="coroa"):
		t = t + 0
	a = input("face: ").lower()
print(t)