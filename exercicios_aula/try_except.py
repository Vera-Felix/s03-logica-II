try:
    nota = float (input("Qual a sua nota de 0 a 10: "))

    if nota >= 7:
        print ("Aprovada")
    else:
        print("Reprovada")

except:
    print("Você precisa digitar um número entre 0 e 10")