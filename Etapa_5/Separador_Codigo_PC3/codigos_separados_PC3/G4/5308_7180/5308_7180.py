x = float(input("Numero x: "))
k = int(input("Numero k: "))

c =1
s = 0


while (c<=k):
	s =  s + c/(2*c*x)
	c = c + 1
print(round(s,10))