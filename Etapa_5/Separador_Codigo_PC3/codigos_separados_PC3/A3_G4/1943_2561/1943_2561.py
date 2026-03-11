# Isoleucina
# C6 H13 N O2

# Metionina
# C5 H11 N O2 S

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

molecula = input()
if (molecula.lower() == "isoleucina"):
	peso = C * 6 + H * 13 + N + O * 2
if (molecula.lower() == "metionina"):
	peso = C * 5 + H * 11 + N + 2 * O + S

print(round(peso, 2))
	