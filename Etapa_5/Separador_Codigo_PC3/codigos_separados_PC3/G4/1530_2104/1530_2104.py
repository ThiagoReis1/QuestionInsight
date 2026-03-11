peg = int(input("pegaminhos:"))
var = int(input("varinhas:"))
cpeg = float(input("cresc. pegaminhos:"))
cvar = float(input("cresc. pegaminhos:"))
total = peg+var
armazen = 80000
anos = 0 
while (total<armazen):
	peg = ((peg*cpeg)/100)+peg
	var = ((var*cvar)/100)+var
	anos = anos+1
	total = peg+var

print(anos)

