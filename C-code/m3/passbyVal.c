#include<stdio.h>

int swap(int aval, int bval)
{
	int temp;
	temp = aval;
	aval = bval;
	bval = temp;
	return(100);
}
int swap2(int aval, int bval)
{
	int temp, count;
	for(count = 0; count < 4; count++)
	{
	temp = aval;
	aval = bval;
	bval = temp;
	}
	return(100);
	
}
void print(int aval[], int bval[])
{
	int count;
	for(count = 0; count < 4; count++)
	printf("aval[%d] is %d, bval[%d] is %d\n", count, aval[count], count, bval[count]);
}
int main()
{
	int val1 = 200, val2 = 34;
	int returned = 1;
	int arr1[] = {1,3,5,7};
	int arr2[] = {3,9,15,21};
	printf("returned: %d val1 is: %d, val2 is:%d\n", returned, val1, val2);
	returned = swap(val1, val2);
	printf("returned: %d val1 is: %d, val2 is:%d\n", returned, val1, val2);
	returned = swap2(val1, val2);
	printf("returned: %d val1 is: %d, val2 is:%d\n", returned, val1, val2);
}
