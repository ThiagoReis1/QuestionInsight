hort=3.85
lat=2.95
enl=7.90
i=0
total=0

setor=input().upper()

while i < len(setor):
	if setor[i] == 'H':
		total= total + 3.85
	elif setor[i] == 'L':
		total = total + 2.95
	elif setor[i] == 'E':
		total = total + 7.90
	i = i + 1
print (round(total,2))