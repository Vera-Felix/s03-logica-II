print ("Olá, obrigada por ligar para nós")
print ("Caso você queira falar com nossos departamentos digite")
print ("Financeiro = 1. Administrativo = 2. Recursos Humanos = 3. Assistência Técnica = 4: ")

resultado = int (input("Digite o número do departamento: "))

if resultado == 1:
    print("Você será direcionada para o Financeiro")
elif resultado == 2:
    print("Você será direcionado para o Administrativo")
    if resultado == 3:
        print("Você será direcionado para o Recursos Humanos")
else:
    print ("Você será direcionado para a Assistência Técnica")