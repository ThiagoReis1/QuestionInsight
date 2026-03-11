from numpy import*
saque = array(eval(input('')))
cont = zeros(3, dtype=int)#saques acima do limite
sl = 0

for i in range(size(saque)):
	if(saque[i] >= 2000):
		sl = sl + 1
		
print(sl)

ps = 0

for i in range(size(saque)):
	p = -1
	if(saque[i] >= 2000):
		print(i)
