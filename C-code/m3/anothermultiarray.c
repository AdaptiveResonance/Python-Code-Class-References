#include<stdio.h>

void print(int arr1[][3])//?rows x 3 columns. Print through each integer
{
	int col, index;
	for(index = 0; index < 3; index++)
	{	
		for(col = 0; col < 3; col++)
		{
			printf(" %d", arr1[index][col]);
		}
		printf("\n");
	}
}
void multi2by(int arr1[][3])//double each variable function
{
	int index, col;
	for(index = 0; index < 3; index++)
	{	
		for(col = 0; col < 3; col++)
		{
			arr1[index][col] *= 2;// a = a * 2;
		}
	}
}
int main()
{
	int array[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
	int array1[4] = {1,2,3,4};
	
	printf("address of array: %p\n", array);
	print(array);//print 3D array 
	multi2by(array);//multiply by 2
	print(array);     //pass first address of array to function protoype above
}
