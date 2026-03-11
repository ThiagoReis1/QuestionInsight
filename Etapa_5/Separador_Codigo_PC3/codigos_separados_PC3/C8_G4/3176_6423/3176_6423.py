
v = input("").upper()
x = 0
y = 0
i = 0
for i in range(len(v)):
	if v[i]=="A" or v[i]=="E" or v[i]=="I" or v[i]=="O" or v[i]=="U":
		x+=1
	else:
		y += 1
	i+=1
print(x)
print(y)