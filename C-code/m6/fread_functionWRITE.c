#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>

 

extern int errno;

 

int main(int numargs, char *theargs[])
{
    FILE *fileptr; // file pointer
    char array[45];    
    fileptr = fopen(theargs[1], "w+");
    
    if(fileptr == NULL)
    {
        fprintf(stderr, "Get it right: %s\n", strerror(errno));
        exit(-1);
    }
    
    for(int count = 0; count < 44; count++)
    {
        scanf("%c", &array[count]);
        fwrite(&array[count], 1, 1, fileptr);
    }
    array[44] = '\0';
    fprintf(stdout, "\tString in the file: %s I am at pos: %ld\n", array, ftell(fileptr));

 

    fseek(fileptr, 0, SEEK_SET);
    //fseek(fileptr, -16, SEEK_END); // go to the end and go back 16 
                                     //   and then read from there
    char array1[45] = {'\0'};
    fread(array1, 44, 1, fileptr); // The file pointer is still 
                                   //   at the end of the file
                                   // Read will fail to read anything
    fprintf(stdout, "\n\tString in the file: %s\n", array1);
    fclose(fileptr);
}
