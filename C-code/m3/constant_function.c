#include<stdio.h>

	//int adder (int arg1,int arg2,int arg3,int arg4);   //prototype
	
	int adder(int arg1,int arg2,int arg3,int arg4)
	{
		return(arg1 + arg2 + arg3 + arg4);
	}
	int main()
	{
		int result = adder(1,2,3,4);
		//int result = 10;
		int num = printf("result is: %d\n", result);
		printf("Num: %d\n", num);
	}

