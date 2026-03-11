from numpy import*

roda = array(eval(input("manda ai: ")))

i = 0
p = 100

while i < size(roda):
	if roda[i] == 1:
		p = p * 5
	if roda[i] == 2:
		p = p * 3
	if roda[i] == 3:
		p = p
	if roda[i] == 4:
		p = p / 2
	i += 1
print (p)

livin on my vain
	
