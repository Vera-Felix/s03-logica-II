# 1o. O maior número:
print("Olá! Seja bem-vindes!")
a = int(input("Digite um número (de 0 a 10): "))
b = int(input("Digite outro número (de 0 a 10): "))

if a > b:
    print("O maior número é " + str(a))
elif b > a:
    print("O menor número é " + str(b))
else:
    print("Os números são iguais")