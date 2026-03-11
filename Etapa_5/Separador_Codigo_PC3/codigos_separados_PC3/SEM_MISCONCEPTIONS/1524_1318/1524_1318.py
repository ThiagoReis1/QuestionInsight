qt = int(input())
qx = int(input())
qy = int(input())
quantAtual =  qt 
count = 0
while(quantAtual > 0 ):
	quantContaminada = qx - qy
	quantAtual = quantAtual + quantContaminada
	count = count + 1

	
print(count)