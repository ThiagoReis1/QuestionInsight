num = int(input())
menores = 0
s = 1
while (num!=-1):
	menores = menores + 1
	num = int(input())
	while(num<18 and num>0):
		menores = menores + 1
		s = s + menores
print(s)
	