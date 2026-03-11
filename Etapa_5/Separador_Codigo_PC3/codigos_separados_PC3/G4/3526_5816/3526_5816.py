x = float(input(": "))
k = int(input(": "))
ac = 0
i = 0
while(i != k):
	ac = ac + ( (x ** (2*i + 1)) / (2*i + 1) )
	i = i + 1
print(round(ac,7))