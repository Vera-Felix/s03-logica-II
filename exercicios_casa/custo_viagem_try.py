print ("Bem-vindo ao nosso sistema de cálculo de custo de viagem.")

# entradas
nome = input("Qual seu nome? ")
# variáveis
viagem = 20

try:
    km_viajados = float(input("Quantos km você viajou? "))

    if km_viajados < 0:
        print ("Por favor digite números positivos.")
    elif km_viajados < 50:
        print ("Não calculamos valores menores que 50km.")
    elif km_viajados <= 200:
        print ("Olá,"  + nome + "!"" Sua viagem custará R$ ", viagem + km_viajados * 0.75)
    elif km_viajados <= 500:
        print ("Olá,"  + nome + "!"" Sua viagem custará R$ ", viagem + km_viajados * 0.60)
    else:
        print ("Olá,"  + nome + "!"" Sua viagem custará R$ ", viagem + km_viajados * 0.50)

except:
    print ("Entre com um valor válido.")