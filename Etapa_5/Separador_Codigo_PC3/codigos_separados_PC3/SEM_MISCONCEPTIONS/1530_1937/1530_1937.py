pergaminhos = int(input("Pergaminhos: "))
vara = int(input("Varinhas: "))
perp = float(input("Percentual pergaminho: "))
perv = float(input("Percentual varinhas: "))

#---------

t = 0
quant = 0


#----------

while(quant <= 80000):
	pergaminhos = pergaminhos + (perp/100)*pergaminhos
	vara = vara + (perv/100)*vara
	quant = pergaminhos + vara
	
	
	t = t + 1
	
print(t)
	