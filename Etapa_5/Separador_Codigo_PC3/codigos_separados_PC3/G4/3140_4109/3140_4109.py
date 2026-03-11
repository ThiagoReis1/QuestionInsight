from numpy import*
x = array(eval(input("Vetores: ")))

i = 0
s = 0

while(len(x)>i):
	s += (x[i]**(5))
	i +=1
print(round((s/size(x))**(1/5), 2))
