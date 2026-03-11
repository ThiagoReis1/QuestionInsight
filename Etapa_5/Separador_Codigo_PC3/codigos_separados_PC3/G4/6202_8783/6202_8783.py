ap=float(input("insira a altura:"))
tc=float(input("taxa de crescimento:"))
ano=0
ab=1.69
tb=0.01
while ap<ab:
	ab=ab+tb
	ap=ap+tc
	ano+=1
print(ano)