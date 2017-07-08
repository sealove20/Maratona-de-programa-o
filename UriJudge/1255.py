import string

alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

#Entrada de dados
tam = int(input())

#função que conta a frequencia de aparacição das letras e adiciona em uma lista
def conta(str, freq):
    for x in range(len(alf)):
        freq.append(str.count(alf[x]))


for k in range(tam):

    n = input()
    freq = []
    str = n.lower()#função para alterar a string para caixa baixa
    conta(str, freq)
    m = max(freq)#função que retorna o valor máximo da lista

    for i in range(len(alf)):
        if freq[i] is m:
            print(alf[i], end='')
    print()
