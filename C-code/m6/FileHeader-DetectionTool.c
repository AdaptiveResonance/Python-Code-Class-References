#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<errno.h>
//a.out filename
//Basic file header reader
void decoder(char *bigbuff)
{
	char msg[41];
	for(int index = 0; index < 41;index++)
	{
	if (bigbuff[index]=='\0')
			{break;}
		
		msg[index]=(bigbuff[index])^(0x33);
		
	}
	printf("decoded message is: %s", msg);
}

int main(int argc, char *argv[])
{
	char file[30] = {0};
	strcpy(file, argv[1]);
	FILE *fileptr; // file pointer 
    fileptr = fopen(file, "r");
    if(fileptr == NULL)
    {
        fprintf(stderr, "there is an error in file path: %s\n", strerror(errno));
        exit(-1);
    }
    char buffer[5];
    fread(buffer, 1, 4, fileptr);
    
    if(buffer[0] == 0x31 && buffer[1] == 0x35 && buffer[2] == 0x30 && buffer[3] == 0x20)
    {
    	printf("im in testing diagnostic\n");//left this in for diagnostic
    }
    if(buffer[0] == 0x7F && buffer[1] == 0x45 && buffer[2] == 0x4C && buffer[3] == 0x46)
    {
    	printf("option 1 This is an ELF file\n");
    }
    if(buffer[0] == 0x59 && buffer[1] == 0x52 && buffer[2] == 0x41 && buffer[3] == 0x47)
    {
    	printf("option 2 This is a YRAG file\n");
    }
    fseek(fileptr, 0x3C, SEEK_SET);
    fread(buffer, 1, 4, fileptr);
    char bigbuff[41] = "\0";
    fseek(fileptr, -4, SEEK_CUR);
    fread(bigbuff, 1, 40, fileptr);
    int num = atoi(buffer);
    printf("The 4byte string at offset 0x3c is: %s in integer value it is:%d\n", buffer, num);
    printf("The extended string at offset 0x3c is: %s\n", bigbuff);
	decoder(bigbuff);
}
