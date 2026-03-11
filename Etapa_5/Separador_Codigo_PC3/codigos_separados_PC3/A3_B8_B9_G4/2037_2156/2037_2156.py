i = int(input("Idade dos participantes"))

m = 0
t = 0

while (i != -1):
	if(i >= 18):
		i = int(input("Idade dos participantes"))
	elif(i < 18):
		i = int(input("Idade dos participantes"))
		
		t = t+1
print(t)