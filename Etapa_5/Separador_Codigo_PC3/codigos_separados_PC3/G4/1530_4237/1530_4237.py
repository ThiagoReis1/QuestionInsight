perg = int(input("Pergaminhos: "))
var = int(input("Varinhas: ")) 
pp = float(input("Percentual perga: ")) 
pv = float(input("Percentual varinha: "))

anos = 0

while(perg+var<80000):
	perg = perg*(pp/100) + perg
	var = var*(pv/100) + var
	anos = anos + 1 
	
print(anos)
	