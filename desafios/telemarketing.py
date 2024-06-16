
numero = int (input("Olá! Obrigada por ligar para nós. Financeiro, digite 1. Administrativo, digite 2. Recursos Humanos, digite 3. Assistência Técnica, digite 4: "))

if numero == 1:
    print("Você será direcionada para o Financeiro")
elif numero == 2:
    print("Você será direcionado para o Administrativo")
    if numero == 3:
        print("Você será direcionado para o Recursos Humanos")
else:
    print ("Você será direcionado para a Assistência Técnica")

    

