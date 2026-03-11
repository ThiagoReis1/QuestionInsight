from numpy import*

j = array(eval(input("Faces jogadas: ")))
p = 0
i = 0

while i < size(j):
	if j[i] == 1:
		p = p + 10
	if j[i] == 2:
		p = p + 5
	if j[i] == 3:
		p = p + 0
	if j[i] == 4:
		p = p + 5
	if j[i] == 5:
		p = p + 20
	if j[i] == 6:
		p = p + 10
	i = i + 1
print(p)
		
	