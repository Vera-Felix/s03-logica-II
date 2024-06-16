print("Olá. Bem-vindes ao nosso sistema de calculo do IMC. Vamos calcular o seu IMC?")

# Perguntas inciais para o calculo
nome = input("Qual seu nome? ")
peso = float(input("Qual seu peso? Utilize ponto para casas decimais: "))
altura = float(input("Qual sua altura? Utilize ponto para casas decimais: "))

# Calculo IMC
imc = peso / (altura**2)

# Determina a classificação com base no IMC calculado
if imc < 18.5:
    classificacao = "Magresa"
elif 18.5 <= imc <= 24.9:
    classificacao = "Normal"
elif 25.0 <= imc <= 29.9:
    classificacao = "Sobrepeso"
elif 30.0 <= imc <= 39.9:
    classificacao = "Obesidade"
else:
    classificacao = "Obesidade grave"

print("Oi,"+ nome +"! Sua classificação é de " + classificacao + ".")
