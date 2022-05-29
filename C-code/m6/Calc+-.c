#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//incomplete
//CMD calculator for adding/subtracting using atoi.
//little input validation so use format below:
	/*./cmdline1  “hello” + “World” + “Good Times”
	hello World Good Times
	./cmdline1 100 + 200 + 300 – 400
	200*/
int check (char *args[])//returns 0 for number or 1 for string
int nums( int argc, int *argi, char *args[]);
int convert(int argc, char *args[])//convert strings to integer
int strngs(int argc, char *args[])
	
int main (int argc, char *args[])
{
	//printf("%s: %d  %c\n", args[1], argc, args[1][0]);
	int arg = check(args);//returns 0 for number or 1 for string
	//printf("action is %d\n", arg);
	int argi[argc];//#of arguements
	if (arg == 0)
	{
	convert(argc, args);
	}
	if (arg == 1)
	strngs(argc, args);
}
int check (char *args[])//returns 0 for number or 1 for string
{
	//printf("%s: %d  %c\n ", args[2], argc, args[2][0]);
	//printf("checking %c is %d\n",args[1][1], args[1][1]);
	if(args[1][1] <= 57 && args[1][1] >= 48)	
	{		//48-57 ascii
	//printf("Number!\n");
		return(0);
	}
	else
	{	
	//printf("it's a string starting with %s\n", args[1]);
		return(1);
	}
}
int convert(int argc, char *args[])
{
	int argi[argc];
	for(int index = 0; index < argc-1; index++)
	{
	//argi[index]=args[index]-48;
	argi[index] = atoi(args[index+1]);
	//printf("args was %s argi is now %d \n",args[index+1], argi[index]);
	}
	nums(argc, argi, args);
}
int nums( int argc, int *argi, char *args[])
{
	int answer = argi[0];
	int index=2;
	for(index = 2; index < argc-1; index=index+2)
	{
		if(args[index][0] == '+')
		{
			answer = answer + argi[index];
		}	
		if(args[index][0] == '-')
		{
			answer = answer - argi[index];
		}
	}
	printf("Final answer is: %d\n", answer);
}
int strngs(int argc, char *args[])
{
	int index=1;
	int index2=0;
	char newarr[argc][10];
	for (index = 1; index < argc; index++)
	{
	//printf("index is %d checking strngs: %s count is %d\n",index, args[index], argc);
		//for (index2 = 0; args[index][index2] != '\0'; index2++)
		//{
		//printf("hello im in a loop. indexes are %d %d and string is %s\n",index, index2, args[index]);
		strcpy(newarr[index-1], args[index]);
		
			if (args[index][index2] >= 65 && args[index][index2] <= 90)
			{
				//printf("%c", args[index][index2]);
				printf("%s ", newarr[index-1]);
			}
			if (args[index][index2] >= 97 && args[index][index2] <= 122)
			{
				//printf("%c", args[index][index2]);
				printf("%s ", newarr[index-1]);
			}
		//}
	}
}