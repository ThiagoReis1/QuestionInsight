perg = int(input("")) #qtd de pergaminhos
var = int(input("")) #qtd de varinhas
pp = float(input("")) #percentual de cresc de pergaminhos
pv = float(input("")) #percentual de crec de varinhas
rp = pp/100 #razao de crec de pergaminhos
rv = pv/100 #razao de cresc de varinhas
t = 0  #num de anos
while(perg + var <= 80000):
	perg += perg*rp
	var += var*rv
	t += 1
print(t)