x = float(input())
k = int(input())
cont = 0
s = 0
while cont<k:
	cont = cont + 1
	s = s + (cont/x)
print(round(s,10))