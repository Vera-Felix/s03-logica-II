print ("Bem-vindo ao nosso sistema de cálculo de custo de viagem.")

# entradas
nome = input("Qual seu nome? ")
km_viajados = float(input("Quantos km você viajou? "))

# variáveis
viagem = 20
    
if km_viajados <= 200:
    print ("Olá,"  + nome + "!"" Sua viagem custará R$ ", km_viajados + viagem * 0.75)
elif km_viajados <= 500:
    print ("Olá,"  + nome + "!"" Sua viagem custará R$ ", km_viajados + viagem * 0.60)
else:
    print ("Olá,"  + nome + "!"" Sua viagem custará R$ ", km_viajados + viagem * 0.60)