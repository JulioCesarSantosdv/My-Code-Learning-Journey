"""
Elabore um programa que leia o ano de nascimento de uma pessoa
e que seja capaz de dizer a sua idade.
=========================================================================
Entendimento:
1.Estabelecer a leitura do ano de nascimento pela variável 'nascimento'
2.Estabelecer a leitura do ano atual pela variável 'ano'
3.Calcular a idade com base na fórmula: 'idade = ano - nascimento'
4.Escrever a idade da pessoa.
"""

from datetime import date
nascimento = int(input('Por favor, digite o ano que você nasceu: '))
ano = date.today().year
idade = ano - nascimento
#print('Você está com {} anos de idade! '.format(idade))
print(f'Você está com {idade} anos de idade!')