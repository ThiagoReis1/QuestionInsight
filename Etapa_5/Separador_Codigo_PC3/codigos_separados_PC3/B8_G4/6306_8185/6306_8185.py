from numpy import*

v = input("Vetor(ALP): ").upper()

i = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0

while (i < len(v)):
	if v[i] == "A":
		i2 = i2 + 19.9
		i5 = i5 + 1
	elif v[i] == "L":
		i3 = i3 + 3.50
		i6 = i6 + 1
	elif v[i] == "P":
		i4 = i4 + 4.25
		i7 = i7 + 1
	i = i + 1
	
total = i2 + i3 + i4
print(round(total, 2), i5, i6, i7)
		
	
		
			
				
		