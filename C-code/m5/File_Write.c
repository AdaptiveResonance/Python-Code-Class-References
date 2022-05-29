#include<stdio.h>
#include<stdio.h>
#include <stdlib.h>
#include <string.h>

extern int errno;
int main()
{
	FILE *fileptr;	//file pointer to access a file
	char input [45];
	fileptr = fopen("text2.txt", "w");	//Open text2.txt in reading mode
										//when fopen executes it creates a data structure and
										//reference to that data struct
										//
										
	//testing if file opened without errors
	if(fileptr == NULL)
	{
		fprintf(stderr, "The file didn't open: %s [*] %d\n", strerror(errno), errno);
        for(int count = 0; count < 10; count++)
            fprintf(stderr, "\n%s\n", strerror(count));
		exit(-1);
	}
	printf("Please enter a string to write to file:");
	scanf("%[^\n]s", input);
	
	fprintf(fileptr, "%s", input);
	for (int count =0; count <sizeof(input); count++)
		fprintf(fileptr, "%c", input[count]);
		
	fclose(fileptr); //always close file before program ends...
	return(0);
}
