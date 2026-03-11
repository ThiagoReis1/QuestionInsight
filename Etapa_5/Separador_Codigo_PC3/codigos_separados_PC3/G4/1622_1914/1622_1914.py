from numpy import*
ent = array(eval(input("")))
s = array(eval(input("")))
i = 0
p = 0
while(i<size(ent)):
	p = p + ent[i] - s[i]
	if(p>75):
		p = 75
	i = i + 1
print(p)