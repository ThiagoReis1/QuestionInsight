s=input("produtos: ")
i=0
total=0

while i < len(s):
	if s[i] == "C":
		total = total + 10.50
	if s[i] == "E":
		total = total + 8.75
	if s[i] == "P":
		total = total + 17.90
		
	i = i + 1
print(round(total,2))
	