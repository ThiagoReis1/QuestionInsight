ac = float(input())
ta = float(input())

altura_macaco = 1.86
taxa_macaco = 0.01
ano = 0

while ac <= altura_macaco:
	altura_macaco = altura_macaco + taxa_macaco
	ac = ac + ta
	ano = ano + 1

print(ano)