ac = 1.5
tc = 0.02
ap= float(input())
tp= float(input())
ano = 0
while(ap<ac):
	ac= ac+tc
	ap= ap+tp
	ano += 1
print(ano)