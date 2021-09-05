/*Desvio Condicional Composto em C*/

#include <stdio.h>

void main()
{
   float n1,n2,media;
   printf("Por gentileza, digite a primeira nota: \n");
   scanf("%f", &n1);
   printf("Por gentileza, digite a segunda nota: \n");
   scanf("%f", &n2);
   media = (n1+n2)/2.0;
   if(media>=7.0){
       printf("Aluno(a) Aprovado(a)! \n");
   }
   else{
       printf("Aluno(a) Reprovado(a)! \n");
   }
}
