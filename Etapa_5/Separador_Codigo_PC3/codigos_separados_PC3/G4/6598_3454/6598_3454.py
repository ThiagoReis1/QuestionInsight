# faça seu código aqui!

n = int(input())
tais = 0
edgar = 0
ana = 0

while n > 0:
	voto = input().lower()
	if voto == 'edgar':
		edgar += 1
	elif voto == 'tais':
		tais += 1
	else:
		ana += 1
	n-=1

print('tais=', tais)
print('edgar=', edgar)
print('ana=', ana)