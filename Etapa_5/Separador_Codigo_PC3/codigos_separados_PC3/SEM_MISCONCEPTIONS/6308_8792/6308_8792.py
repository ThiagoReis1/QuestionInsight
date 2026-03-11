from numpy import*

secao = input('').upper()
seq = ''
i = 0

while i < len(secao):
	if secao[i] == 'A':
		seq = seq[i] * 16.75
	if secao == 'L':
		seq = seq[i] * 4.60
	if secao == 'P':
		seq = seq[1] * 2.85
	i += 1


print(round(seq,2))