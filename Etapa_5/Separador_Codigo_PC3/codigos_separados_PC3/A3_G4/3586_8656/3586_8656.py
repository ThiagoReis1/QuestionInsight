from numpy import*

anel = array(eval(input()))

i = 0

while i < size(anel):
	if anel[i] == 1:
		p = 100
	if anel[i] == 2:
		p = 60
	if anel[i] == 3:
		p = 20
	if anel[i] == 4:
		p = 0
		
	i = i + 1
print(p)