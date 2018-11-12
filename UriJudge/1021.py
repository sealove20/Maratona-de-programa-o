x = float(input())
x = x + 0.001
if x >= 0 and x<= 1000000.00:
  valores = [100, 50, 20, 10, 5, 2]
  moedas = [1.0, .5, .25, .10, .05, .01]

  print('NOTAS:')

  for i in valores:
    valores = x // i
    print('{} nota(s) de R$ {:.2f}'.format(int(valores), i))
    x %= i

  print('MOEDAS:')

  for i in moedas:
    moedas = x // i
    print('{} moeda(s) de R$ {:.2f}'.format(int(moedas), i))
    x %= i