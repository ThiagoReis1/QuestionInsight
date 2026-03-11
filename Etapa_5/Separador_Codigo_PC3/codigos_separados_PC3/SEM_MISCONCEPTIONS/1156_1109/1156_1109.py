celcan = float(input("digite numero inicial de células cancerosas: "))
taxa = float(input("taxa percentual de reducao: "))
novacelcan = float(input("digite numero de novas celulas cancerosas: "))
limite = 500000
soma = 0
i = 1
while(celcan <= limite):
	celulaselim = celcan * taxa
	celcan = celcan - celulaselim + novacelcan
	soma = soma + celcan
	i = i + 1
print(i)
	
	