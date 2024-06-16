print ("Bem-vindes ao departamento de trânsito!")

# Solicita a velocidade do veículo e a velocidade máxima permitida
velocidade_veiculo = float (input("Indique a velocidade do veículo em km/h: "))
velocidade_maxima = float (input("Indique a velocidade máxima da via em km/h: "))

# Calcula a diferença percentual da velocidade do veículo em relação à velocidade máxima permitida
percentual = ((velocidade_veiculo - velocidade_maxima) / velocidade_maxima) * 100

# Verifica se houve excesso de velocidade e calcula a multa, se aplicável
if velocidade_veiculo > velocidade_maxima:
    if percentual <=20:
        multa = 200
        print("Você ultrapasou a velocidade máxima da via em 20%. Sua multa é de R$ 200,00")
    else:
        percentual <=30
        multa = 350
        print("Você ultrapasou a velocidade máxima da via em 30%. Sua multa é de R$ 350,00")
else:
    print("Você está dentro da velocidade permitida. Continue dirigindo com segurança.")



