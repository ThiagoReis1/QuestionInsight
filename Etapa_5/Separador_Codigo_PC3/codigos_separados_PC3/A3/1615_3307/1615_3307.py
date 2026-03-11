from numpy import* 

j1 = array(eval(input('Vetor de aneis de j1: ')))
j2 = array(eval(input('Vetor de aneis de j2: ')))

i = 0 # cont
anel1 = 0 
anel2 = 0
anel3 = 0
anel4 = 0
pontj1 = 0
while i < size(j1):
	if j1[i] == 1:
		anel1 = anel1 + 1
	if j1[i] == 2:
		anel2 = anel2 + 1
	if j1[i] == 3:
		anel3 = anel3 + 1
	if j1[i] >= 4:
		anel4 = anel4 + 1
	i = i + 1
	pontj1 = anel1 * 40 + anel2 * 20 + anel3 * 10 + anel4 * 0
i = 0
pontj2 = 0
anel1 = 0 
anel2 = 0
anel3 = 0
anel4 = 0
while i < size(j2):
	if j2[i] == 1:
		anel1 = anel1 + 1
	if j2[i] == 2:
		anel2 = anel2 + 1
	if j2[i] == 3:
		anel3 = anel3 + 1
	if j2[i] >= 4:
		anel4 = anel4 + 1
	i = i + 1
	pontj2 = anel1 * 40 + anel2 * 20 + anel3 * 10 + anel4 * 0
if pontj1 > pontj2:
	print('JOGADOR UM')
elif pontj2 > pontj1: 
	print('JOGADOR DOIS')
else:
	print('EMPATE')

		
	