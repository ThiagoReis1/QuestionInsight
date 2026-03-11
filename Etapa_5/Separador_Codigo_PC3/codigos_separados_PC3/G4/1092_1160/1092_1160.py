x = int(input())
a = x//100
ra = x%100
b = ra//10
rb = ra%10
c = rb
prop = (a**3 + b**3 + c**3)
if(x == prop):
	print(prop, "atende a propriedade")
else: 
	print(prop)