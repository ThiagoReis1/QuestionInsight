hm = 1.86
tm= 0.01

hc = float(input())
tc = float(input())

x = 0

while hc < hm:
	hm += tm
	hc+= tc
	
	x += 1
	
print(x)