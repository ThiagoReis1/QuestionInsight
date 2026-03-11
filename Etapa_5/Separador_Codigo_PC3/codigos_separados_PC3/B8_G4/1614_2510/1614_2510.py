from numpy import*
a=array(["BANANA","BIFE","FEIJOADA","OMELETE","TOMATE"])
c=array([0.97,2.95,1.27,1.04,0.2])
alimentos = array(eval(input("Alimentos: ")))
y = array(eval(input("Qtde: ")))
i = 0
k = 0
while i<size(alimentos):
	if alimentos[i]==a[0]:
		k = k + c[0]*y[i]
		i=i+1
	elif alimentos[i]==a[1]:
		k = k + c[1]*y[i]
		i=i+1
	elif alimentos[i]==a[2]:
		k = k + c[2]*y[i]
		i=i+1
	elif alimentos[i]==a[3]:
		k = k + c[3]*y[i]
		i=i+1
	elif alimentos[i]==a[4]:
		k = k + c[4]*y[i]
		i=i+1
print(k)