choice = int(input())

if(choice < 7):
	resposta = "eh menor"
if(choice == 7):
	resposta = "eh fortuna"
if(choice > 7):
	resposta = "eh maior"
	
print(resposta)