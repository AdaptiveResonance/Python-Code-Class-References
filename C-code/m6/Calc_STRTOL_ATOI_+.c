#include <stdio.h>
#include <stdlib.h>
//CMD adder/calc using strtol or atoi comparison
 
void addsit(char **argv, int argc, int *num, int *sum)
{
    for(int idx = 1; idx < argc; idx += 2) //go up by twos
    {
        printf("%s: %d\n", argv[idx], *argv[idx]);
        num[idx/2] = atoi(argv[idx]);   // atoi converts character array to integer
        printf("\tnum[%d] = %d\n", idx/2, num[idx/2]);
        *sum += num[idx/2]; // 3 = a + r
    }
}

int main(int argc, char *argv[])
{
    int num[argc];  // creating array with enough space for numbers
    int sum=0;
    
    addsit(argv, argc, num, &sum);
    //sum = addsit(argv, argc, num);
    printf("\t ---- Sum is %d\n ----", sum);
    
    sum = 0;
    for(int idx = 1; idx < argc; idx += 2)
    {
        printf("%s: %d\n", argv[idx], *argv[idx]);
        num[idx/2] = strtol(argv[idx],0,10);   // strtol converts character array to integer
        printf("\tnum[%d] = %d\n", idx/2, num[idx/2]);
        sum += num[idx/2];
    }
    printf("Total sum is: %d\n", sum);
    printf("%s\n", argv[1]); // We are printing a string. is because the argv[1] is an address
    //printf("Sum of %d number is: %d\n", argc - 1, sum);
    return 0;
}
