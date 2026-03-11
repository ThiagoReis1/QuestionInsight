pm = int(input())
cont = 0
cont0 = 0
while (pm == -1):
	pm = int(input())
	if (pm >= 35):
		cont0 = cont0 + 1
		pm = int(input())
	if (pm <= 95):
		cont = cont + 1
		pm = int(input())
		
c = (pm + pm) / (pm + pm)
print(c)
		 