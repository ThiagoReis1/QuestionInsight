resposta1 = input("foi um bom atendimento?... ").upper()
t = 0
while (resposta1 != "S"):
	if (resposta1 == "SIM"):
		resposta1 = input("foi um bom atendimento?... ").upper()
		t = t + 1
	else:
		resposta1 = input("foi um bom atendimento?... ").upper()
print(t)