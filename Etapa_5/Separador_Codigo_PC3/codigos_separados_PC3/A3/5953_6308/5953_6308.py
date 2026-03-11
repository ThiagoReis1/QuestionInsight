tipo = input()
refeicao = int(input())
refris = int(input())
total = 0.0

if tipo == 'L':
	total = refeicao * 6.0 + refris * 3.0

if tipo == 'P':
	total = refeicao * 13.5 + refris * 3.0

print(total)