# Pergunta inicial para obter a temperatura em graus Celsius
temperatura_celsius = float(input("Qual a temperatura atual em graus Celsius? "))

# Determinação da classificação do dia com base na temperatura
if temperatura_celsius > 27:
    classificacao = "dia quente"
elif 20 <= temperatura_celsius <= 27:
    classificacao = "dia agradável"
else:
    classificacao = "dia frio"

# Exibição do resultado
print(f"Com {temperatura_celsius:.1f} graus Celsius, hoje está classificado como {classificacao}.")