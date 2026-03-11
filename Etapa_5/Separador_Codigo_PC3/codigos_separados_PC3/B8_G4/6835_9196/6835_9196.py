m= input("produto:").upper()

k= len(m)
i= 0
g= 0
while i< k:
	if m[i]=="B":
		g= g + 3.75
	elif m[i] == "C":
		g= g + 7.90
	elif m[i]== "E":
		g= g+ 9.85
	i= i+1
print(round(g,2))