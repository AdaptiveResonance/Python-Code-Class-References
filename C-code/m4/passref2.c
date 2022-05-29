#include <stdio.h>

int getVals(int arr1[20], int arr2[20])     //int is return type, getvals is function name, then parameters
{
	arr1[0] = 200;
	arr1[1] = 150;
	arr1[5] = 300;
	return(2000);				//can return value or pointer to an array but not an array as it must be single value
}

int main()
{
	int arr2[20];
	int arr1[20];
	int val;
	printf("arr2[0]= %d\n",arr2[0]);									
	printf("arr2[1]= %d\n",arr2[1]);
	printf("arr2[5]= %d\n",arr2[5]); 
	printf("val: %d\n", val);
	val = getVals(arr2,arr1);     //arr2 and arr1 are equal now// array 2 here is represented by arr2 at the top
	printf("arr2[0]= %d\n",arr2[0]);									
	printf("arr2[1]= %d\n",arr2[1]);
	printf("arr2[5]= %d\n",arr2[5]);
	printf("val: %d\n", val);					//int val would now = 2000 (return value)
}
