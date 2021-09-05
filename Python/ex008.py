"""
Leia quatro valores numéricos inteiros e apresente o resultado das adições
e das multiplicações utilizando o mesmo raciocínio aplicado quando do uso
de propriedades distributivas para a máxima combinação possível entre quatro
variáveis.Não é para calcular a propriedade distributiva, apenas para usar sua
forma de combinação.Considerando a leitura dos valores para as variáveis A,B,C e D
devem ser feitas 6 adições e 6 multiplicações, ou seja A com B;A com C; A com D,
B com C ;B com D, C com D.
================================================================================
Entendimento
1.Fazer a leitura A,B,C,D   7.Fazer que A6 receba C+D  13.Fazer que M6 receba C*D
2.Fazer que A1 receba A+B   8.Fazer que M1 receba A*B  14.Escreva A1,A2,A3,A4,A5,A6
3.Fazer que A2 receba A+C   9.Fazer que M2 receba A*C  15.Escreva M1,M2,M3,M4,M5,M6
4.Fazer que A3 receba A+D  10.Fazer que M3 receba A*D
5.Fazer que A4 receba B+C  11.Fazer que M4 receba B*C
6.Fazer que A5 receba B+D  12.Fazer que M5 receba B*D
"""
A = int(input('Informe um número: '))
B = int(input('Informe um número: '))
C = int(input('Informe um número: '))
D = int(input('Informe um número: '))
A1 = A+B
A2 = A+C
A3 = A+D
A4 = B+C
A5 = B+D
A6 = C+D
M1 = A*B
M2 = A*C
M3 = A*D
M4 = B*C
M5 = B*D
M6 = C*D
print(f'{A1},{A2},{A3},{A4},{A5},{A6}'
      f'\n{M1},{M2},{M3},{M4},{M5},{M6}')
