"""
Elaborar um programa que leia o valor numérico correspondente ao salário mensal
(SM) de um trabalhador e também faça a leitura do valor do percentual de reajuste
(PR) a ser atribuído. Apresente o valor do novo salário(variável NS)
===============================================================================
Entendimento:
1.Ler o valor de um salário como número real(SM)
2.Ler do percentual de reajuste(PR)
3. Calcular novo salário (NS) NS=SM+SM*PR/100
4.Escreva NS
"""
CO = (input('Informe o nome do colaborador: '))
SM = float(input('Informe o salário do colaborador:R$ '))
PR = float(input('Informe o percentual para reajuste: '))
NS = SM+(SM*PR/100)
print(f'O salário do colaborador {CO} que era de R${SM:.2f} mensais, \n'
      f' com o reajuste de {PR:.0f}% passará a ser de R${NS:.2f}.')