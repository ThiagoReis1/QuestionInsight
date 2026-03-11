play = input("insira uma face:")
random = 0
while(play != -1):
	if(play == 6):
		random = random+1
	play = int(input("faces:"))
print(random)