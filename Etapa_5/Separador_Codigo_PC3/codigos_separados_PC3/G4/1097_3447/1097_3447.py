v = int(input())
a = v // 100000
ra = v % 100000
b= ra // 10000
rb = ra % 10000
c = rb //1000
rc = rb % 1000
d = rc // 100
rd = rc % 100
e = rd // 10
re = rd % 10
f = re // 1
x = (a*100) + (b*10) + (c*1)
y = (d*100) + (e*10) + (f*1)

w = (x - y) ** 2
if(w == v):
	men= 'atende'
	print(men)
	print(v)
	
else:
	men= 'nao atende'
	print(men)
	print(v)
	