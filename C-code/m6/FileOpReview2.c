#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<errno.h>

 

#define WIDTH 20

 

int main()
{
    char file[WIDTH];
    printf("Please enter a filename: ");
    scanf(" %[^\n]s", file);
    
    FILE *fptr = fopen(file, "r");
    if(fptr == NULL)
    {
        fprintf(stderr, "Dude where's my ... file : %s\n", strerror(errno));
        exit(1);
    }
    char buffer[5]; // 4 for magic number and 1 for null terminator...
    
    fread(buffer, 1, 4, fptr); // Read four bytes into buffer. 
    
    printf("Values read from file:-%s-\n", buffer);

 

     for(int count =0; count< 4; count++)
        printf("%#04x ",buffer[count]);// # means place 0x in front 02 print with 2 character minimum
                                       //     and pad if necessary. 0xa pad to this 0x0a
    printf("\n");
    
    printf("File position %ld\n",ftell(fptr));
    
    fseek(fptr, 0x7, SEEK_SET); // seek to file position offset 7 from the beginning of the file.
    printf("File position %ld\n",ftell(fptr));    
    char retchar = fgetc(fptr);
    printf("seventh offset is: %#04x\n", retchar);
    
    // 0x12 == 18
    fseek(fptr, 18, SEEK_SET); // seek to file position offset 7 from the beginning of the file.
    printf("File position %ld\n",ftell(fptr));    
    short retshrt;
    fread(&retshrt, 2, 1,fptr); // 1byte - 8bits, 2bytes - 16bits (short), 4bytes - 32bits (integer)
    printf("Eigthenth offset is: %#06x\n", retshrt);
     printf("Eigthenth offset is: 0x%06x\n", retshrt);
    
    fclose(fptr);
}
