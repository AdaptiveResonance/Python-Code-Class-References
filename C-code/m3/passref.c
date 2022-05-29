#include<stdio.h>

int hello(char arr[])
{
	printf("address of first element of array arr: %p\n", arr);
	printf(arr);
	return(0);
}

int main()	//start here in main, the above hello reference function is already in memory :)
{	
	char arr[] = "hello%s%x\n";       
	
	printf("address of first element of array arr: %p\n", arr);
	hello(arr);				//call hello and send the address of H
	
	hello("goodbye%s%x\n");
	
	return(0);
}
