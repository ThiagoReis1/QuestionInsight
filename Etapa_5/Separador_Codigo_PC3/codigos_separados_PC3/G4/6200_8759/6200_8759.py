cicero = 1.75
taxa= 0.01
maxx=float(input())
taxx=float(input())
ano=0
while maxx< cicero:
	ano= ano+1
	cicero= cicero + taxa
	maxx= maxx + taxx
print(ano)