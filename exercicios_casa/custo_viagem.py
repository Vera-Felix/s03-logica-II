print ("Bem-vindo ao nosso sistema de cálculo de custo de viagem.")

# entradas
nome = input("Qual seu nome? ")
km_viajados = float(input("Quantos km você viajou? "))

# variáveis
viagem = 20

# custo viagem:
if km_viajados <= 200:
    custo = viagem + km_viajados * 0.75
elif viagem <= 500:
    custo = viagem + km_viajados * 0.60
else:
    custo = viagem + km_viajados * 0.50

# Exibe o resultado formatado
print("Olá,"  + nome + "!"" Sua viagem custará R$ ", custo)