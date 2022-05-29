#include<stdio.h>
#include<stdlib.h>
#include<string.h>

 

int main()
{
    char file[25];
    
    printf("Please enter a filename: ");
    scanf(" %[^\n]s", file);
    FILE *ptr = fopen(file, "w+"); // a r w a+ r+ w+ 

 

    if(ptr == NULL)
    {
        fprintf(stderr, "Hey there file named: %s not found\n", file);
        exit(-1);
    }
    
    char arr[] = "Hello World";
    fwrite(arr, 1, strlen(arr), ptr); // write causes the file indicator to be at the end of the file
    //fseek(ptr, 0, SEEK_SET); // This bring us to the beginning of the file    
    fseek(ptr, 0, SEEK_END); // this brings us to the end.SEEK_SET - beginning SEEK_CUR - current SEEK_END - end
    int size = ftell(ptr);
    printf("Size of file in bytes: %d\n", size);
    char array[size+1];
    fseek(ptr, 0, SEEK_SET); // This bring us to the beginning of the file    
    fread(array, 1, size, ptr);
    array[size] = '\0';
    printf("Array is: %s\n", array);
    fclose(ptr);
}
