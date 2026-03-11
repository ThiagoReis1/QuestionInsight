li = input("Escolha os produtos que deseja: ").upper()
i = 0 
d = 0
s = 0
g = 0
t = len(li) - 1
while i <= t:
	if li[i] == "D":
		d = d + 1
	elif li[i] == "S"	:
		s = s + 1
	elif li[i] == "I"	:
		g = g + 1
	i += 1
t = d*2.25 + s*4.00 + g*6.90
print(round(t,2))