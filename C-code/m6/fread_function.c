#include<stdio.h>
#include<stdlib.h>
#include<errno.h>
#include<string.h>

 

extern int errno;

 

int main(int numargs, char *theargs[])
{
    FILE *fileptr; // file pointer
    char array[45];    
    fileptr = fopen(theargs[1], "r");
    
    if(fileptr == NULL)
    {
        fprintf(stderr, "Get it right: %s\n", strerror(errno));
        exit(-1);
    }
    int index = 0;
    int val = 1;
    //fread(location to store to, size of each entity, number of each entity, where to read from);
    while(val)
    {
        val = fread(&array[index], 1,1,fileptr);
        fprintf(stdout, "Index: %d %c \t read: %d\n",index, array[index], val);
        index++;
    }
    
}
