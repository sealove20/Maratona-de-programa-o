a, b, c = input().split()
maior = ((int(a)+int(b))+abs(int(a)-int(b)))/2
if maior == int(a):
    maior = ((int(a) + int(c)) + abs(int(a) - int(c))) / 2
elif maior == int(b):
    maior = ((int(c) + int(b)) + abs(int(c) - int(b))) / 2
print(int(maior),"eh o maior")
