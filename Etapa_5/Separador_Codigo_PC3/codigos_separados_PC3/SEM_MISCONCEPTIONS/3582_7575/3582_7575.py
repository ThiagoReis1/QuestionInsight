from numpy import*

p=array(eval(input("custo dos itens: ")))

i=0
total=0
while i<size(p):
	if p[i]>160.0:
		total=p[i]+total-25
	else:
		total=total+p[i]
	i=i+1
print(total)
