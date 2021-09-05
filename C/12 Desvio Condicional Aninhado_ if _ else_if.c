/*Desvio Condicional Aninhado - if / else if em C*/

#include <stdio.h>

int main()
{
    float n1,n2,media;
    printf("Digite a primeira nota:  \n \n ");
    scanf("%f", &n1);
    printf("Digite a segunda nota:  \n \n ");
    scanf("%f", &n2);
    media = (n1 + n2) / 2.0;
    if (media >= 7.0){
        printf("Aluno(a) aprovado(a)!\n");
        
    }
    else{
        if (media >= 5.0){
            printf("Aluno(a) em recuperação!\n");
            
        }
        else{
            printf("Aluno(a) reprovado(a)!\n");
            
        } 
    return 0;
        
    }
    
}
    
       
   
       
   

