"""
Elabore um programa de computador que calcule a área de uma circunferência
e apresente a medida da área calculada.
============================================================================
Entendimento
Obs.: Para fazer o cáculo da área de circunferência, é necessário conhecer
primeiro a fórmula que executa o cálculo, sendo A =πR², em que A é a variável
que conterá o resultado do cálculo da área,π é o valor da constante
Pi(3.14159265) e R o valor da variável que representa o raio.Basta estabelecer
o seguinte:
1.Ler um valor para o raio, no caso variável R
2.Estabelecer que pi venha possuir o valor 3.14159265
3.Efetuar o cáculo da área, elevando ao quadrado o valor de R e
multiplicando esse valor por pi
4.Apresentar o valor da variável A.
"""

r = float(input('Digite um valor qualquer: '))
pi = 3.14159265
a = (r**2)*pi
print(f'O valor da medida da área calculada é de {a}.')

