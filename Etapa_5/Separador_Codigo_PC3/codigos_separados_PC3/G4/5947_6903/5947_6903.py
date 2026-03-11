op = input("'C' para coxinha e 'E' para esfirra: ").upper()
qse = int(input("quantidade de coxinha ou esfirra: "))
qs = int(input("quantidade de sucos: "))

if op == 'C':
	t = qse*2 + qs*6
	print(round(t,2))
else: 
	t = qse*4.5 + qs*6
	print(round(t,2))