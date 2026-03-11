from numpy import*

s = input().upper()

# VARIAVEIS LOOP

i = 0 # percorrer string
c = float(0) # custo da senha

while (i < len(s)):
	
	if (s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U"):
		
		c = c + 1.12
		
	else:
		
		c = c + 1.18
	
	i = i + 1

print (round(c, 2))