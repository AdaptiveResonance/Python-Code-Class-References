#include<stdio.h>
#include<stdlib.h>
#include<string.h>

 

void openfile(FILE **fptr, char *fname)
{
    *fptr = fopen(fname, "r");
    if(*fptr == NULL)
    {
        fprintf(stderr, "How dare you ... \n");
        exit(-1);
    }
}
int readContents(FILE **fptr, char *array)
{
    return (fread(array, 1, 16, *fptr));  // read 16 bytes from the file
}

 

int main(int argc, char *argv[])
{
    char filename[24];
    
    if(argc > 1)
    {
        strcpy(filename, argv[1]);
    }
    else
    {
        printf("Please enter a filename: ");
        scanf(" %[^\n]s", filename);
    }

 

    FILE *ptr; // ptr currently store 0xF4321 some random value
    openfile(&ptr, filename);    
    
    // after testing the line below declare the array as "unsigned char"
    char arr16bytes[16]; // Please check to see what happens if you don't have an unsigned array

 

    readContents(&ptr, arr16bytes);
//    printit(args);
    
    // Print the first 16 bytes
    for(int idx = 0; idx < 16; idx++)
    {
        //if(arr16bytes[idx] > 32 && arr16bytes[idx] <= 0x7E)
            printf("%02x ", arr16bytes[idx]); // this print 16 bytes on a line
        //else
            //printf(".");
    }
    
    printf("\n");
    fclose(ptr);    
}
