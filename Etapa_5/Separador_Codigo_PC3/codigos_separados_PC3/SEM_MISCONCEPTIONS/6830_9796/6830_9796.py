produto = input("[H]->hortifruti\n[L]->laticinios\n[E]->enlatados\n")
i=0
total=0
while i<len(produto):
	if produto[i] == 'H':
		total = total+3.85
	if produto[i] == 'L':
		total = total+2.95
	if produto[i] == 'E':
		total = total+7.90
	i+=1
print(round(total,2))
