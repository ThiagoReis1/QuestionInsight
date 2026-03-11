from numpy import*
x= input()
i = 0
c = 0
c1 =0
c2 = 0
c3 = 0
while i <len(x):
	if x[i] == "B":
		c = c+ 3.75
		c1= c1+1
	elif x[i] == "C":
		c = c + 7.90
		c2 = c2 +1
	elif x[i] == "E":
		c = c + 9.85
		c3= c3 + 1
	i = i+1
x = round(c,2)
print(x,c1, c2,c3)