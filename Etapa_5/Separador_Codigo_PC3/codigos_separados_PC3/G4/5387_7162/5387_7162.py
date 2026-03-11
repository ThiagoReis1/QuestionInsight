# Leitura da string
s = input("Digite a string").upper()

i=0 # Variável contadora
t=0 # Variável acumuladora

while i<len(s):
	if s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i]=="O" or s[i]=="U":
		t = t + 45.12
		i=i+1
	else:
		t=t+50.18
		i=i+1
		
print(round(t,2))		

