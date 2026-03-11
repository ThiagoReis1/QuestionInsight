from numpy import*

v= array(eval(input("digite o valor do item: ")))

b=0

for i in range (size(v)):
			if (v[i])>50:
				v[i]=v[i]*(8/100)

b = sum(v)
	
print(round(b,2))
			