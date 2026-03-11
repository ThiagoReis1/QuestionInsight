altura_joe = 1.77
taxa_joe = 0.02
n=float(input())
m=float(input())
ano =0

while(n >= altura_joe):
	altura_joe=altura_joe+taxa_joe
	n=n+m
	ano=ano+1
	
	print(ano)