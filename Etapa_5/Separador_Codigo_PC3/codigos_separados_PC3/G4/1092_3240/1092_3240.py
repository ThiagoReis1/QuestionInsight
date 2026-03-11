d = int(input())

d1= d // 100
r1 = d % 100
d2= r1 //10
d3= r1 % 10


c = (d1 **3) +(d2**3) + (d3**3)

if(d == c):
	print("correto")
else:
	print("incorreto")
	