from numpy import* 

x = array(eval(input("digite os valores: ")))

i = 0 
s = 0 

while i < size(x):
	if x[i] > 160:
		z = x[i] - 25
		s = s + z
	elif x[i]:
		s = s + x[i]
	i = i + 1 

		
print(round(s, 2))
