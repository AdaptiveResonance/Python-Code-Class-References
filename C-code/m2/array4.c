#include<stdio.h>

void main (void)
{
	int index;
	char array2[5] = {'h'};
	
	int array[5] ={1,2};
	for(index = 0; index < sizeof(array)/sizeof(int); index++) //=5 coded this way allows for array updates
		printf("array[%d] = %d\n",index, array[index]);     // last part prints the contents in array OF the index number
		
		for(index = 0; index < sizeof(array2)/sizeof(char); index++)
		printf("array2[%d] = %c\n",index, array2[index]);		
		
	array2[3] = 'l';                              //change the third char to l
	printf("address of: %p, value: %c address of: %p\n", array2, array2[0], &array2[0]);

}
