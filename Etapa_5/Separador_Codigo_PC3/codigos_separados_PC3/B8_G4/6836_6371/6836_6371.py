s = input().upper()

cB = 0
cC = 0
cM = 0
i = 0

while i<len(s):
	if s[i]=='B':
		cB+=1
	elif s[i]=='C':
		cC+=1
	elif s[i]=='M':
		cM+=1
	i+=1
vB = cB*6.80
vC = cC*11.75
vM = cM*5.90
t = vB+vC+vM
print(round(t,2))