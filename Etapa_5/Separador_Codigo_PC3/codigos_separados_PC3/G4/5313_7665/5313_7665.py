n=int(input())
tot=7206.14
ano=2018
while(tot<n):
	tot=tot+(65/100*tot)
	ano=ano+1
print(ano)