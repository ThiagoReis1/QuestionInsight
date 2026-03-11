ent = input("entrada:")

p = "preta"
t = 0

while(ent != "s".upper()):
	if(ent == p.upper()):
		t = t + 1
		ent = input("entrada:")
	else:
		ent = input("entrada:")
print(t)		

	
