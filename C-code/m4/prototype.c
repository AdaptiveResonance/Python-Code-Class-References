#include<stdio.h>

int printer(int B);// this creates references for the bottom functions for when main calls

int main()// main can now remain near the top
{
	printer();
	printer();
	int A = printer();
}

int printer(int B)
{
	printf("hola\n");
	return(1)
	//more stuff here
}
