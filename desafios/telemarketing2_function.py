print ("Olá, obrigada por ligar para nós. Caso você queira falar com nossos departamentos:\n")

def mostra_menu():
    print ("Financeiro, digite 1.")
    print ("Administrativo, digite 2.")
    print ("Recursos Humanos, digite 3.") 
    print ("Assistência Técnica, digite 4.\n")

def escolhe_menu():

    resultado = int (input("Digite o número do departamento:\n"))

    if resultado == 1:
        print("Você será direcionada para o Financeiro.")
    elif resultado == 2:
        print("Você será direcionado para o Administrativo.")
    elif resultado == 3:
            print("Você será direcionado para o Recursos Humanos.")
    elif resultado == 4:
        print ("Você será direcionado para a Assistência Técnica.")
    else:
        print("Opção invalida. Por favor, digite um numero de 1 a 4.")

mostra_menu()
escolhe_menu()