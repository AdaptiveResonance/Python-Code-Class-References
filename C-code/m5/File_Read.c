#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<errno.h>

extern int errno;

int main()
{
    FILE *fileptr;   // File pointer to access a file
    char input[45];
    
    fileptr = fopen("text3.txt", "r"); // open file for reading
    
    if(fileptr == NULL)
    {
        fprintf(stderr, "The file didn't open: %s [*] %d\n", strerror(errno), errno);
        for(int count = 0; count < 10; count++)
            fprintf(stderr, "\n%s\n", strerror(count));
        exit(-1);
    }
    char aByte;
    
    while(fscanf(fileptr, "%c", &aByte) != EOF)
    {
        fprintf(stderr, "%c",aByte); 
        fseek(fileptr, 11, SEEK_CURR);  //check also fread(); 
    }
    
    return(0);
}
