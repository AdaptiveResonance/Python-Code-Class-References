#include<stdio.h>

int main()
{
	int array[8] = {1,2,3,4,5,6,7,8};
	int count = 0;
	char arr[] = {"hello-------"};
	char arr2[4][5] = {};
	//step1
	scanf("%[^\n]s",arr);
	scanf("%[^\n]s",arr2); //&arr2[0]
	//step2
	//printf("array2 is %s", array2[0] )
	
	//printf("Sizeof arr: %ld", sizeof(arr));   //32
	
	int temp;
	for(count = 0; count < sizeof(arr)/sizeof(int); count+=1)    //2 for int array if switch each couple ex. switch 1 and 2
	{
		arr[count] = arr[count] +1;
		//temp = array[count];
		//array[count] = array[count+1];
		//array[count+1] = temp;
	}
}
