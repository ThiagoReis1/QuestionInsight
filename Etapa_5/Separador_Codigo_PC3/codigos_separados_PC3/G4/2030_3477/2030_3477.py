m =  input("lado da moeda: ").upper()

c= 0

while(m != "S"):
	if (m == "CARA"):
		c = c + 1
	m =  input("lado da moeda: ").upper()
print(c)	
