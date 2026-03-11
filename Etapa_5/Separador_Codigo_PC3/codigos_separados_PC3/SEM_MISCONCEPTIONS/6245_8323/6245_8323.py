psq = input().upper()
count = 0

while psq != "X":
	if psq == "S":
		count = count+1
	psq = input().upper()
print(count)