#valor das cenouras R$ 1.20 - do que cinco cenouras;
#cinco cenouras ou mais = * R$ 0.90;

cenourinha = int(input(" quantas cenouras foram compradas: "))

if cenourinha < 5:
	valor = cenourinha * 1.20
	
else:
	valor = cenourinha  * 0.90
	
print(round(valor,2))