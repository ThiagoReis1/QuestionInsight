string= input("Insira uma string:").upper()
i=0
total=0

while i < len(string):
	if string[i]== "A":
		total= total + 19.9
	elif string[i]== "L":
		total= total + 3.5
	elif string[i]== "P":
		total= total + 4.25
	i= i +1
	
print(round(total, 2))
