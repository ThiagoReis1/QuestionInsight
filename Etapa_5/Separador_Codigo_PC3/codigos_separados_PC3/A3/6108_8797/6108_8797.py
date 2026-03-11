a = float(input("combustivel"))

total = 0 

if a<17.5:
	total =  a + 1.5
elif 17.5<a<35:
	total =  a + 2.3
elif 35<a<50:
	total =  a + 3.3
else:
	total =  a + 4.7
print(round(total , 2))