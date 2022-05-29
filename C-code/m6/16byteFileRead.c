#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <errno.h>

//a.out textfile.txt 4
int print(char *buffer, int offsetcount)
{
	printf("%08x\t", offsetcount);
		offsetcount = offsetcount + 16;
    	for(int count =0; count < 16; count++)
		{
			if(buffer[count] == NULL)
			{
				break;
			}
			else
			printf("%02x ",buffer[count]);
		}
		printf("\t");
		for(int count =0; count < 16; count++)
		{
			if(buffer[count] == NULL)
			{
				break;
			}
			if(buffer[count] <= 32 || buffer[count] == 127)
			{
				printf(".");
			}
			else
			printf("%c", buffer[count]);
		}
		printf("\n");
		return(offsetcount);
}
int dump (char *file, int *offset)
{
	FILE *fileptr; // file pointer 
    fileptr = fopen(file, "r");
    if(fileptr == NULL)
    {
        fprintf(stderr, "there is an error in file path: %s\n", strerror(errno));
        exit(-1);
    }
    
    char buffer[17] = "\0";
    char mirror [17] = "\0";
	int offsetcount = *offset;
	fseek(fileptr, 0, SEEK_END);
	int size = ftell(fileptr);
	fseek(fileptr, *offset, SEEK_SET);
	for(int index = 0; index < size - *offset; index = index+16)
	{
		strcpy(buffer, mirror);
		fread(buffer, 1, 16, fileptr);
		offsetcount = print(buffer, offsetcount);
	}
    fclose(fileptr);
}
int main(int argc, char *argv[])
{
		char filename[30] = {0};
		strcpy(filename, argv[1]);
		int offset = 0;
		if(argc > 2)
		{
			offset = atoi(argv[2]);
		}
		dump(filename, &offset);
}
