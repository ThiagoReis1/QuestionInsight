b = input("insira b: ").upper()

V = 0
E = 0
D = 0
n = 0
while(n!="X"):
	b = input("insira a: ").upper()
	if(b == "V"):
	   V = V + 3
	elif(b == "D"):
	   D = D + 1
	elif(b == "E"):
	   E = E + 0
	elif(a == "X"):
	   n == "X"
	
k = (V + E + D)/100
print(round(k,2))