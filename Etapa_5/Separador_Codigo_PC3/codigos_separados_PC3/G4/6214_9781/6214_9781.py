ENT = int(input())
N = 0

while(ENT != -1):
	if(ENT >= 45) and (ENT <= 150):
		N += 1
	ENT = int(input())

print(N)