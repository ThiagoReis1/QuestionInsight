n=int(input())
i=0
ho=-1**0.5
pot=2
while(i<n):
    s=pot*ho
    ho=(2-2*(1-(ho**2/4))**0.5)**0.5
    pot=5*pot
    i=i+1
print(round(s, 5))