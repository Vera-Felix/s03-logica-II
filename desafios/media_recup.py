print ("Bem-vindes a verificação de Notas")
# Pedindo as notas dos bimestres
nota1 = float(input("Digite a nota do 1º bimestre (de 0 a 10): "))
nota2 = float(input("Digite a nota do 2º bimestre (de 0 a 10): "))

# calculo media
media = (nota1 + nota2) / 2

# verificando se aluna está aprovada, em recuperação ou reprovada.
if media >= 7:
    print("Aprovada")

elif media >= 6:
    print ("Recuperação")
# verificando se aluna passou na recuperação
    nota_recuperacao = float(input("Qual sua nota da recuperação: "))
    if nota_recuperacao >=6:
        print("Aprovada na recuperação")
    else:
        print("Reprovada na recperação")

else:
    print ("Reprovada")