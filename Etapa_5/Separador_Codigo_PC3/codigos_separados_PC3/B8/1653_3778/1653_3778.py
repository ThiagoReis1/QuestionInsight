from numpy import*
res = zeros(5, dtype=int)
pessoas = input()
pessoas = pessoas.replace(",", "")
pessoas = pessoas.replace(" ", "")
for i in range(0, len(pessoas), 2):
	if pessoas[i] == "A" and pessoas[i+1] == "R":
		res[0] = res[0] + 1
	elif pessoas[i] == "B" and pessoas[i+1] == "R":
		res[1] = res[1] + 1
	elif pessoas[i] == "C" and pessoas[i+1] == "L":
		res[2] = res[2] + 1
	elif pessoas[i] == "C" and pessoas[i+1] == "O":
		res[3] = res[3] + 1
	elif pessoas[i] == "U" and pessoas[i+1] == "Y":
		res[4] = res[4] + 1
print(max(res))
print(res)