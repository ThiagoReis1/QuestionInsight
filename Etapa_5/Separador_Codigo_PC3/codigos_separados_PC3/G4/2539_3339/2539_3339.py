v = float(input())
m = float(input())
j = float(input())

s = v
t = 0

if( v > 0 and m > 0 and j > 0):
	while( s < v * 1.2):
		s = s - m + (s * j/100)
		t = t + 1
	print(round(t, 2))
else:
	print("Dados incorretos")

#while( v > 0 and m > 0 and j > 0):
	#m = m + v*j/100
	#t = t + 1

		