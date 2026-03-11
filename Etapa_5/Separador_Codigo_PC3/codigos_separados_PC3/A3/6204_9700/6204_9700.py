altura_macaco = 1.86
taxa_macaco = 0.01
txc = 0.01
alt=float(input())
taxa=float(input())
ano= 0
while alt <=altura_macaco:
	altura_macaco += taxa_macaco
	alt += taxa
	ano +=1
print(ano)