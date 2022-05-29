#include<stdio.h>

int add(int val1,int val2)
{
	return(val1 + val2);
}

int sub (int val1, int val2) //funtion to subtract
{
	printf("address of val1: %p\n", &val1);
	return(val1 - val2);
}

int input()			//function to get user input
{
	int val1;
	printf("Enter > ");
	scanf("%d", &val1);
	return(val1);
}

int main ()

{
	int mval1, mval2, result;
	mval1 = input();				//requests to resolve value for input twice
	mval2 = input();
	result = add(mval1, mval2);
	printf("sum: %d,%d\n", add(mval1, mval2),result);
	result = sub(mval1, mval2);
	printf("sub: %d, %d\n", sub(mval1, mval2),result);
	
	return(0);
}
