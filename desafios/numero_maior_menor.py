# 1o. O maior número:
print("Olá! Seja bem-vindes!")
n1 = int(input("Digite um número (de 0 a 10): "))
n2 = int(input("Digite outro número (de 0 a 10): "))

if n1 > n2:
    print("O maior número é ", n1)
elif n1 < n2:
    print("O menor número é ", n2)
else:
    print("Os números são iguais")