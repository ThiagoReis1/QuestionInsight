ac = 1.5
tc = 0.02
p = 0

h = float(input("altura do cabeca: "))
th = float(input("taxa de crescimento: "))

while (ac > h): 
	ac = ac + tc
	h = h + th
	p = p + 1
print(p)