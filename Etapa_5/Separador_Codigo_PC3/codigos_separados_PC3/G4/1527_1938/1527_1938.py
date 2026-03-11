a = int(input("quantidade inicial do forseti: "))
b = int(input("quantidade inicial do loki: "))
c = float(input("percentual de crescimento forseti: "))
d = float(input("percetual de crescimento loki: "))
i = 1
a = a + a * (c/100)
b = b + b * (d/100)
if(a > 0 and b > 0):
	if(a > b):
		if(c < d):
			while(a >= b):
				a = a + a * (c/100)
				b = b + b * (d/100)
				i = i + 1
		
print(i)	

	
