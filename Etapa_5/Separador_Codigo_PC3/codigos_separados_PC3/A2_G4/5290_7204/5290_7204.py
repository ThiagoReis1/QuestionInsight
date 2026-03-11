n = int(input("face: "))
i = 0
j = 0
while n != -1 :
	if n == 5 :
		i = i + 1
		j = j + 1
		n = int(input("face: "))
	else:
		i = i
		j = j + 1
		n = int(input("face: "))
		
if n == -1 :
	print(j)
	pct = (i/j)*100
	print(pct)