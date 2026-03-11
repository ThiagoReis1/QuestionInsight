from numpy import*
a = array(eval(input("valores: ")))
i = 0
dano = 0
while(i<size(a)):
	dano = dano + a[i]*(i+1)
	i = i + 1
print(dano)	