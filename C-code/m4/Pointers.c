#include<stdio.h>

int main()
{
	int intval = 5;//value
	int *intptr = &intval;//pointer to inval address
	int arr1[5]= {1,23,4,5,6};//array
	
	printf("%p %p\n", intptr, &intval);//same address
	printf("%x %x\n", intptr, intval);//
	
	//Dereferencing is the action of using the pointer in order to reassign the value residing in the original pointed to variable. 
	(*intptr)++;			//change value from 5>>6
	intptr++;				//increase memory space reference
	intptr = &arr1[1];		//setting new reference
	
	printf("%p %p\n", intptr, &intval);
	printf("%x %x\n", *intptr, intval);

	if(ptr)	//if statement to confirm a pointer is NULL or real active pointer
		printf("is indeed a pointer\n");
}
