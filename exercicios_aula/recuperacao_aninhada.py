nota = float (input("Qual a sua nota de 0 a 10: "))

if nota >= 7:
    print ("Aprovada")

elif nota >= 5:
    print ("Recuperação")
    nota_recuperacao = float(input("Qual sua nota da recuperação "))
    if nota_recuperacao >=8:
        print("Aprovada na recuperação")
    else:
        print("Reprovada na recperação")
else:
    print("Reprovada")

print("Fim")