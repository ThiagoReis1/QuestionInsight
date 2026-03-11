from numpy import*
x = array(eval(input("Insira o numero: ")))
i = 0
p = 0
while i< size(x):
	if x[i] == 1:
		p = p + 10
	if x[i] == 2:
		p = p + 5
	if x[i] == 3:
		p = p + 10
	if x[i] == 4:
		p = p + 5
	if x[i] == 5:
		p = p + 10
	if x[i] == 6:
		p = p + 5
	i = i + 1
print(p)