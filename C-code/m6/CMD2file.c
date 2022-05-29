#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
//commandline to file writer/reader
//./cmdline2  -b 100  -e  200 -s  4 -f textfile.txt -m w
//program begin position finish position steps count file path mode read/write
extern int errno;
int read (char file[])
{
	FILE *fileptr; // file pointer 
    fileptr = fopen(file, "r");
    if(fileptr == NULL)
    {
        fprintf(stderr, "error in file path: %s\n", strerror(errno));
        exit(-1);
    }
    char byte = 'Q';
    
    while(fread(&byte, 1, 1, fileptr) != 0)
    {
    	fprintf(stdout, "%c", byte);
    	//fprintf(stdout, "Value: %x char: %c\n", byte, byte);
    }
    printf("\n");
    fclose(fileptr);
}
char adder(char input[], int min, int inter)
{
	sprintf(input, "%d", min+inter);
}
int write (char file[],int min, int max, int inter, int size)	
{
	FILE *fileptr; // file pointer 
    fileptr = fopen(file, "w");
    if(fileptr == NULL)
    {
        fprintf(stderr, "error in file path: %s\n", strerror(errno));
        exit(-1);
    }
    char input[size];
    adder(input, min, 0);
    fprintf(fileptr, "%s", input);
    printf("%s", input);
    fclose(fileptr);
	fileptr = fopen(file, "a");
    for(min; min < max; min=min+inter)
    {
    	
    	adder(input, min, inter);
    	//printf("looping min: %d max: %d inter: %d current: %s\n", min, max, inter, input);
		fprintf(fileptr, " %s", input);
		printf(" %s", input);
    }
    fclose(fileptr);
    printf("\n");
    printf("would you like to read it?");
    scanf("%1[^\n]c",input);
    printf("%s", input);
    if (input[0]=='y'|| input[0]=='Y')
    {
    	printf("\n");
    	read(file);
    }
    else
    exit(1);
}	

int check(int argc, char *args[])
{
	int min = 0;
	int max = 0;
	int inter = 0;
	char mode = 'x';
	int index = 1;
	char file[40];
	int size = 1;
	for (index = 1; index < argc; index = index+2)
	{
		switch(args[index][1])
		{
			case 'b':
				min = atoi(args[index+1]);
				printf("min:%d\n", min);
				break;
			case 'e':
				max = atoi(args[index+1]);
				printf("max:%d\n", max);
				size = max;
				break;
			case 's':
				inter = atoi(args[index+1]);
				printf("Step Count:%d\n", inter);
				break;
			case 'f':
				strcpy(file, args[index+1] );
				printf("File Path is:%s\n", file);
				break;
			case 'm':
				mode = (args[index+1][0]);
				printf("Mode is:%c\n", mode);
				break;			
		}
	}
		if (mode=='r')
			read(file);
		if (max == 0 || min == 0 || inter == 0)//is min necessary?
		{
			printf("range is missing values. Min:%d Max:%d Step Size:%d\n", min, max, inter);
			exit(1);
		}
		if (max < min+inter)
		{
			printf("step size is too small to run. Min:%d Max:%d Step Size:%d\n", min, max, inter);
			exit(1);
		}
		if (mode=='w')
			write(file, min, max, inter, size);
		if (mode == 'x')
			printf("Mode is missing\n");
			exit(1);
		else
		{
			printf("No mode found!\n");
			exit(1);
		}	
}		
int main (int argc, char *args[])
{
	check(argc, args);	
	exit(1);
}
