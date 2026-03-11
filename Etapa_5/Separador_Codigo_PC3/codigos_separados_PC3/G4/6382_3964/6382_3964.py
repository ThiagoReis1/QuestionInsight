n = eval(input())

for i in range(len(n)):
	if n[i] == 9:
		n[i] = 0
	else:
		n[i] = (n[i]+1)**2
	

print(str(n).replace(",",""))