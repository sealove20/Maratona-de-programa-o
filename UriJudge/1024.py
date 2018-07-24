qtd = int(input())

if qtd >= 1 and qtd <= 10**4:
    for i in range(qtd):
        frase = input()
        if len(frase) <= 10**3:
            fraseCript = ''
            meio = len(frase)//2

            for letra in frase:
                if ord(letra) >= 65 and ord(letra) <= 90:
                    fraseCript += chr(ord(letra)+3)
                elif ord(letra) >= 97 and ord(letra) <= 122:
                    fraseCript += chr(ord(letra)+3)
                else:
                    fraseCript += letra

            fraseCript = fraseCript[::-1]

            aux = fraseCript[0:meio]

            for i in range(meio,len(frase)):
                aux += chr(ord(fraseCript[i])-1)
            print(aux)