#include<stdio.h>

int main()
{
	int intval = 100;
	char chval = 'A';
	
	int *ptrval = &intval;//integer pointer
	char *ptrchr = &chval;//char pointer
	
	printf("address of interval: %p %p\n", &intval, ptrval);//both print intval address
	printf("address of chrrval: %p %p\n", &chval, ptrchr);	//both print the character address
	
	printf("value of intval: %d\n", *ptrval);
	*ptrval = 65;//'A' in ascii
	//Dereferencing is the action of using the pointer in order to reassign the value residing in the original pointed to variable. 
	printf("value of intval: %d\n", *ptrval);			//print new contents
	
	ptrval++;
	ptrchr++;
	printf("address of interval: %p %p\n", &intval, ptrval);// moved up, out there
	printf("address of interval: %p %p\n", &chval, ptrchr);	//char now point to int array
	printf("value of intval: %d\n", *ptrval);//decimal of a pointer is no good and changes on runtime based on new addresses
	printf("value of chrval: %c\n", *ptrchr);//prints new A
}
