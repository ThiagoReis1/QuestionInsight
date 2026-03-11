N = int(input("digete a quantidade de ingrediente: "))

votos_churrasco = 0
votos_lasanha = 0
votos_panquecas = 0
voto = 0
c = 0
while c < N:
	voto = input()
	if voto == "L":
		voto_lasanha = voto_lasanha += 1
	if voto == "C":
		voto_churrasco = voto_churrasco += 1
	if voto == "P":
		voto_panquecas = votos_panquecas += 1
	c+=1
print("l" = voto_lasanha)
print("c" = voto_churrasco)
print("p" = voto_panquecas)