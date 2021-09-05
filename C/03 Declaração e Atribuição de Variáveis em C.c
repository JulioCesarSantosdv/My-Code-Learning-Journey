/*Declaração e Atribuição de Variáveis em C*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
   
   int idade;
   float salario,valor;
   idade = 25;
   
   valor = 4500.50;
   salario = valor;
   printf("Idade: %d\n",idade);
   printf("E o salario: %f\n",salario);
   
   return 0;
}

/* OBS.: O tipo float tem por padrão a precisão de 6 casas decimais*/