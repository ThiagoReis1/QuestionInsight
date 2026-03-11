numr = float(input("numero real:"))
numk = int(input("numero inteiro"))
soma = 0
k = 0 
while(k<numk):
	n = (2*k+2)*numr
	soma = soma + (k+1)/n
	k = k + 1
print(round(soma,10))