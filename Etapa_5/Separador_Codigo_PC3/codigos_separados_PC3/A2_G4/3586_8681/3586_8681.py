from numpy import *

a = array(eval(input("INSIRA O VALOR DO ANEL: ")))

i = 0
p = 0

while i < size(a):
	if a[i]==1:
		p = p + 100
	if a[i]==2:
		p = p + 60
	if a[i]==3:
		p = p + 20
	if a[i]==4:
		p = p
	i = i + 1
print(sum(p))