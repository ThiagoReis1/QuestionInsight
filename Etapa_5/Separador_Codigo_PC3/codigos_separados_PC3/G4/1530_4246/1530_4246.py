perg = int(input('qtd de pergaminhos: '))
var = int(input('qtd de varinhas magicas: '))
pP = float(input('percentual de pergaminhos: '))
pV = float(input('percentual de varinhas: '))
limite = 80000
anos = 0

while((perg + var < limite) and (perg > 0) and (var > 0)):
	acP = perg * (pP/100)
	perg = perg + acP
	acV = var * (pV/100)
	var = var + acV
	anos = anos + 1
print(anos)