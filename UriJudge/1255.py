n = int(input())
palavra = ''
maior = 0
for i in range(n):
    texto = input()
    if len(texto) < 200: #verifíca a quantidade máxima de caracteres
        for j in range(len(texto)):
            cont=0
            for k in range(len(texto)):
                letra = texto[j].lower()
                if letra == texto[k]:
                    cont +=1

            if j == 0:
                contMaior = cont

            #verificação do caracter com maior número de ocorrencias na string
            if cont > contMaior:
                maior = letra
                contMaior = cont
                palavra = ''
                palavra = maior
            elif cont == contMaior:
                palavra += letra
                contMaior = cont

        # listaNova=''
        # for k in range(len(lista)-1):
        #     if k == 0:
        #         letraCmp = lista[0]
        #     elif lista[k] != lista[k+1]:
        #         listaNova += lista[k]

        print(palavra)

