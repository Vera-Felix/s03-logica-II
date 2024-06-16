print("Olá colaboradora. Seja bem-vinde ao nosso sistema de cálculo de salário")

# Perguntas iniciais para o cálculo
nome = input("Qual seu nome? ")
salario = float(input("Qual seu salário? "))
vendas = float(input("Qual seu valor em vendas? "))

vendas1 = vendas * 0.10
vendas2 = vendas * 0.15
vendas3 = vendas * 0.18

# Determinação da comissão com base nas vendas
if vendas <= 3000:
    comissao = vendas1
elif vendas <= 5000:
    comissao = vendas2
else:
    comissao = vendas3

# Calcula o salário final somando o salário base com a comissão
salario_final = salario + comissao

# Exibe o resultado formatado
print(f"Este mês você receberá R$ {salario_final:.2f}, onde R$ {comissao:.2f} é referente à comissão.")
