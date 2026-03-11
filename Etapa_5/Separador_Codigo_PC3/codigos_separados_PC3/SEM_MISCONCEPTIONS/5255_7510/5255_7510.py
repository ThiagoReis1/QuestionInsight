dados = {"1":17.0,"2":17.5,"3":18.0,"4":20.0}
peso = float(input())
dist = float(input())
cod = input()

total = (peso*25.0 + dist*0.10) * (1.0 +(dados[cod]/100))
print(round(total,2))