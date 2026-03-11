v1 = float(input())
v2 = float(input())
votos = v1 + v2
if (v1>v2):
  print("Ambrosio Rutra")
  print(round(((v1/votos) * 100), 2))
else:
 print("Demelza Olecram")
 print(round(((v2/votos)*100), 2))