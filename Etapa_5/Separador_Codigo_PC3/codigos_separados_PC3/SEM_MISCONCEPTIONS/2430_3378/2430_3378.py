Capital=float(input())
Tempo=float(input())
Juros=3


J=(Capital*Juros*Tempo)/100

M=Capital+J

f=J+M

print(round(f, 2))

