ajoe = 1.77
tjoe = 0.02
ap=float(input("altura da pessoa: "))
tcp=float(input("taxa de crescimento da pessoa:"))
c=0
while ajoe>ap:
	ajoe=ajoe+tjoe
	ap=ap+tcp
	c+=1
print(c)