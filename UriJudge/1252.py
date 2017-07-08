#falta tratar negativos
n,m = map(int, input().split())
lista = []

while n != 0 and m != 0:
    lista = []
    if n > 0  and n < 1000:
        for i in range(1,n+1):
            lista.append(int(input()))
        #print(lista)
        for i in range(n):
            for j in range(n-1):
                #ordenação por MOD de maneira ascendente
                if lista[j]%m > lista[j+1]%m:
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux

                #empate entre par e impar
                if lista[j] % 2 == 0 and lista[j+1]%2 != 0 and lista[j]%m == lista[j+1]%m:
                    aux = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = aux

                #Empate entre impar e impar
                if lista[j] % 2 != 0 and lista[j+1]%2 != 0 and lista[j]%m == lista[j+1] %m:
                    if lista[j] > lista[j+1]:
                        aux = lista[j]
                        lista[j] = lista[j+1]
                        lista[j+1] = aux
                    if lista[j+1] > lista[j]:
                        aux = lista[j+1]
                        lista[j+1] = lista[j]
                        lista[j] = aux

                #empate entre par e par
                if lista[j] % 2 == 0 and lista[j + 1] % 2 == 0 and lista[j] % m == lista[j + 1] % m:
                    if lista[j] > lista[j+1]:
                        aux = lista[j+1]
                        lista[j+1] = lista[j]
                        lista[j+1] = aux
                    if lista[j+1] > lista[j]:
                        aux = lista[j]
                        lista[j] = lista[j+1]
                        lista[j] = aux
        for i in range(len(lista)):
            print(lista[i])
        n, m = map(int, input().split())




