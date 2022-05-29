#include<stdio.h>
//arg2main.out -f 3 -7 		etc on commandline
int main(int argc, char *argv[])//first input is # of argument, then the array of the modifier/inputs
{
	printf("number of args: %d\n", argc);//#of arguements to resolve
	
	for(int idx = 0; idx < argc; idx++)
		printf("argv[%d]: %s\n", idx, argv[idx]);
	return 0;
}
