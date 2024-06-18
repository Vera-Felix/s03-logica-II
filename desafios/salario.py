print("Olá colaboradora. Seja bem-vinde ao nosso sistema de cálculo de salário")

# Perguntas iniciais para o cálculo
nome = input("Qual seu nome? ")
salario = float(input("Qual seu salário? "))
vendas = float(input("Qual seu valor em vendas? "))

# Determinação da comissão com base nas vendas
if vendas <= 3000:
    comissao = vendas * 0.10
elif vendas <= 5000:
    comissao = vendas * 0.15
else:
    comissao = vendas * 0.18

# Exibe o resultado formatado
print("Olá,"  + nome + "!"" Este mês você receberá R$ ", salario + comissao)