nick = input("digite seu nick: ")

if (nick.upper() == "MARIO"):
	msg = "Bem-vindo, defensor do Reino dos Cogumelos!"
	print(msg)
else:
	msg = "Seja bem-vindo, " + nick
	print(msg)