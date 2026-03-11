D = float(input())
TF = float(input())
j = float(input())
acm = 0
c = D
while(c < 0.15*D):
	if(D > 0) and (TF > 0) and (j > 0):
		c = D + j*D - TF
		acm = acm + 1
		round(c, 2)
	else:
		print('Dados incorretos')
print(acm)		
		
