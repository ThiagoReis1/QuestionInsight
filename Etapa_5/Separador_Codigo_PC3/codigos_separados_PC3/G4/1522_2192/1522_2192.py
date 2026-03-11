qi = int(input())
desp = int(input())
qcol = int(input())
r = int(input())

tesouro = qi

t = 1

while(tesouro > 0):
	tesouro = t * (qi + qcol - desp - r)
	t = t + 1 
	tesouro = int(input())
	
print(t)