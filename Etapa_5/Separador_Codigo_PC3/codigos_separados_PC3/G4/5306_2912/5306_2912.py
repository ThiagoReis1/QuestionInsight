x = float(input())
k = int(input())
soma = 0
cont=0
while(cont<k):
	cont+=1
	soma+=x/(2*cont)
	
print(round(soma,8))