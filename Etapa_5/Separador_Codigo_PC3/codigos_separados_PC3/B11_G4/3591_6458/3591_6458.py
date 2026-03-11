from numpy import*

v = array(eval(input("insira seu vetor: ")))

p = 0
i = 0

while i < size(v):
	if v[i] == 1:
		p = p + 10
	if v[i] == 2:
		p = p + 5
	if v[i] == 3:
		p = p + 10
	if v[i] == 4:
		p = p + 5
	if v[i] == 5:
		p = p + 10
	if v[i] == 6:
		p = p + 5
	i+=1
print(p)