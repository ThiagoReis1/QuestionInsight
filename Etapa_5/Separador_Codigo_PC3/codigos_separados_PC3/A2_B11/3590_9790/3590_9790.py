from numpy import*
v = array(eval(input("potuacao: ")))
i = 0
total =0
while i < len(v):
	if v[i] == 1:
		total = total + 10
	if v[i] == 2:
		total = total + 5
	if v[i] == 3:
		total = total 
	if v[i] == 4:
		total = total + 5
	if v[i] == 5:
		total = total + 20
	if v[i] == 6:
		total = total + 10
	i = i + 1
print(round(total,2))