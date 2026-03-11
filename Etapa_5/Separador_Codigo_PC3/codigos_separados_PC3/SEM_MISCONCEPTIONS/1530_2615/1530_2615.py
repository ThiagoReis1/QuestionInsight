pergaminhos = int (input())
varinhas = int (input())
pergpc = float (input())
varpc = float (input())

anos = 0
itens = 0

while (itens <= 80000):
	pergaminhos = pergaminhos + (pergaminhos * (pergpc / 100))
	varinhas = varinhas + (varinhas * (varpc / 100))
	itens = pergaminhos + varinhas
	anos = anos + 1
	
print (anos)
	