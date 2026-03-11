x = float(input("digite x: "))
k = int(input("digite k: "))

i = 0
s = 0

while(i<k):
	s = s + (x**(2*i+1))/(2*i+1)
	i += 1
	
print(round(s,7))