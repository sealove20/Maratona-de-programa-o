n = int(input())

for i in range(n):
    frase = input().upper()
    if len(frase) >= 2 and len(frase) <= 100:
        metade = len(frase)//2
        esquerda = frase[:metade]
        direita = frase[metade:]
        print(esquerda[::-1]+direita[::-1])
