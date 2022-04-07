"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para
organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano,
quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada. Este
laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas
informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia
utilizada e a quantidade de cobaias utilizadas em cada experimento. Faça um programa que leia um
valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um
inteiro que representa a quantidade de cobaias utilizadas e uma letra ('C', 'R' ou 'S'), indicando o tipo
de cobaia (R:Rato S:Sapo C:Coelho). Apresente o total de cobaias utilizadas, o total de cada tipo de
cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o
percentual deve ser apresentado com dois dígitos após o ponto.
"""

casos = int(input("Quantos casos você vai digitar | "))
quantidade_coelhos = 0
quantidade_ratos = 0
quantidade_sapos = 0
for i in range(casos):
    quantidade_cobaias = int(input("Quantidade de cobaias | "))
    tipo_cobaia = input("Tipo da cobaia | ").upper()
    if tipo_cobaia == "C":
        quantidade_coelhos += quantidade_cobaias
    elif tipo_cobaia == "R":
        quantidade_ratos += quantidade_cobaias
    else:
        quantidade_sapos += quantidade_cobaias

total = quantidade_coelhos + quantidade_ratos + quantidade_sapos
percentual_coelhos = quantidade_coelhos / total * 100
percentual_ratos = quantidade_ratos / total * 100
percentual_sapos = quantidade_sapos / total * 100

print("""\nRelatorio final
Total | {} cobaias
Total de coelhos | {}
Total de ratos | {}
Total de sapos | {}

Percentual de coelhos | {:.2f}
Percentual de ratos | {:.2f}
Percentual de sapos | {:.2f}
""".format(total,
quantidade_coelhos,
quantidade_ratos,
quantidade_sapos,
percentual_coelhos,
percentual_ratos,
percentual_sapos))
