# Pergunta inicial para obter a temperatura em graus Celsius
print ("Análise do Tempo")
temperatura = float(input("Qual a temperatura atual em graus Celsius? "))

# Determinação da classificação do dia com base na temperatura
if temperatura > 27:
    print("Dia Quente")
elif temperatura > 15:
    print("Dia Agradável")
else:
    print("Dia Frio")