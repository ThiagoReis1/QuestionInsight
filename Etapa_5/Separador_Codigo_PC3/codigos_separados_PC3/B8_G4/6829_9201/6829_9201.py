n = input("digite:").upper()
i = 0 
v = 0

c = 19.90
d = 3.50
f = 4.25

while (i<len(n)):
	if n[i] == "A":
		v+=c
	elif (n[i] == "L"):
		v+=d
	elif(n[i] =="P"):
		v+=f
	i+=1
	
print(round(v,2))
	
