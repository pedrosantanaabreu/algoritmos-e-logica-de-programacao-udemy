"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Uma empresa vai conceder um aumento percentual de
salário aos seus funcionários dependendo de quanto
cada pessoa ganha, conforme tabela ao lado. Fazer um
programa para ler o salário de uma pessoa, daí mostrar
qual o novo salário desta pessoa depois do aumento,
quanto foi o aumento e qual foi a porcentagem de
aumento.

Salário atual Aumento
Até R$ 1000.00 20%
Acima de R$ 1000.00
até R$ 3000.00
15%
Acima de R$ 3000.00
até R$ 8000.00
10%
Acima de R$ 8000.00 5%
"""

# Recebendo valores
salario = float(input("Digite o salário | R$ "))

# Calculando
if salario > 8000:
    porcentagem = 5
elif salario > 3000:
    porcentagem = 10
elif salario > 1000:
    porcentagem = 15
else:
    porcentagem = 20

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

# Exibindo resultado
print("\nNovo salário | R$ {:.2f}\nAumento | R$ {:.2f}\nPorcentagem | {:.2f} %".format(novo_salario, aumento, porcentagem))
