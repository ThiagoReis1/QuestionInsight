from numpy import*

vetor = array(eval(input()))

total = sum(vetor)

for i in vetor:
	if i > 50:
		total = total - (i * 0.08)

print(round(total, 2))