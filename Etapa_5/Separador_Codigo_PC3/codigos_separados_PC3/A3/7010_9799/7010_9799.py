X = int(input('insira o x:'))
Y = int(input('insira o y:'))

lancha = X
somatoria = 0

while lancha <= Y:
	if lancha % 7 == 0:
		print(lancha)
	lancha = lancha + 1
