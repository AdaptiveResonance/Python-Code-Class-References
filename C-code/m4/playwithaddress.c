#include<stdio.h>
#define ROW 3
#define COL 5

int main()
{
int inputs[ROW][COL]={{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15}};
int row=0;
int col=0;


printf("input values are:");
	for(row = 0; row < ROW; row++)
	{
		printf("\nRow %d:  ", row);
		for(col = 0; col < COL; col++)
		{	
			printf(" %d>>  ", inputs[row][col]);
			printf("%d  ", &inputs[row][col]);
		}
	}
	printf("\n");
	printf("%d  ", &inputs[1][0] );
	printf("%d  ", inputs[1] );
	printf("%d  ", &inputs[1] );
	printf("%d  \n", &inputs );   //this one will print out first address of array
	
int intval = 8;
int *ptr = &intval;			//* declares it a int pointer
*ptr = 200;					//target becomes 200, ptr could not be 200 as that would be low level OS memory	

	printf("%d  ", *ptr );  //prints pointed to value 200
	printf("%d  ", &ptr );  //address of pointer itself
	printf("%d  ", ptr);	//address of target intval
	printf("%d  ", intval );//value of intval 200
	printf("%d  \n", &intval );//address of target intval
	
	int *ptr2;
	int arr1[5]={1,3,4,56,8};
	ptr2=arr1;
	
	for(int index=0;index <5; index++)//this is undefined behavior so dont worry, maybe even delete this.
		{
	printf("arr1[%d]+1:%d\n", index+1, ++(*ptr2)); //index 1 is 2
	printf("\tthe *(ptr++): %d\n", *(ptr2+index));  //change refercne to one further
	}
}
/* &array[1][0] is equivalent to  array[1]
   &array[1] is equivalent to  array
   int intVal = 8;
    int *ptr = &intVal;
    *ptr = 200; 
*/



