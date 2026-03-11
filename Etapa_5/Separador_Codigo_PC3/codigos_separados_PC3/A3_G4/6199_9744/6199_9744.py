ac = 1.8
tc = 0.01
ap = float(input())
tp = float(input())
c = 0

while(ap<ac):
	ac = ac +0.01
	ap = ap + tp
	c+=1
print(int(c))
	