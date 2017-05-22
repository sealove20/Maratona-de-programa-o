def fatorial(num):
    total = num
    for i in range(1,num):
        total *= i
    return total


def main():
    num = ''
    while num is not '0':
        num = input()
        # tamanho = len(num)
        if len(num) <= 5 and num != '0':
            decimal = 0
            cont = 1
            for i in range(len(num)-1,-1,-1):
                numeroInt = int(num[i])*fatorial(cont)
                decimal += numeroInt
                cont+=1
            print(decimal)


main()