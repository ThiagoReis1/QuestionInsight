seq = input().upper

soma = 0
c = 0

while(seq != "S"):
	if(seq == "A"):
		soma = 1
	elif(seq == "G"):
		soma = 0
	elif(seq == "C"):
		soma = 0
	elif(seq == "T"):
		soma = 0
	soma = soma + 1
	c = c + 1
print(soma)
	
seq = input().upper