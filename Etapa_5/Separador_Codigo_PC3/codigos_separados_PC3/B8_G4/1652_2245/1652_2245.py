from numpy import*
v = input(": ").split(',')
vetor = zeros(5, dtype = int)
b = 0
pa = 0
pr = 0
a = 0
ind = 0
for i in v:
	if(i.upper() == "B"):
		b = b + 1
	elif(i.upper() == "PA"):
		pa = pa + 1
	elif(i.upper() == "PR"):
		pr = pr + 1
	elif(i.upper() == "A"):
		a = a + 1
	elif(i.upper() == "I"):
		ind = ind + 1
vetor[0] = vetor[0] + b
vetor[1] = vetor[1] + pa
vetor[2] = vetor[2] + pr
vetor[3] = vetor[3] + a
vetor[4] = vetor[4] + ind
if(b > pa) and ( b > pr) and ( b > a) and (b > ind):
	print(b)
elif(pa > b) and ( pa > pr) and ( pa > a) and (pa > ind):
	print(pa)
elif(pr > pa) and (pr > b ) and ( pr > a) and (pr > ind):
	print(pr)
elif(a > pa) and (a  > pr) and (a  > b ) and (a > ind):
	print(a)
else:
	print(ind)
print(vetor)
