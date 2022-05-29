#include<stdio.h>

int main(int argc, char *argv[])
{ 
	printf("starting the parse program: \n");
	if(strcmp(argv[1], "-i")) //compares first arguement to check for '-i' modifier
	{
		printf("Number of loops to run is %S \n", argv[2]);// second passed arguement is evaluated and printed
	}
}
