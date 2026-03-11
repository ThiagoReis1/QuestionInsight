from numpy import*

vet =array(eval(input()))
p = 10000

for i in vet:
	if i == 1:
		p = p *2
	if i ==3:
		p =p/2
	if i==4:
		p=p/4
print(round(p,2))