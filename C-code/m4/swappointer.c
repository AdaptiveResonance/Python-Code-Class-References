#include<stdio.h>
//https://www.tutorialspoint.com/cprogramming/c_passing_pointers_to_functions.htm

void swap1(int *a, int *b)//swap values/contents
{
	int temp = *a;
	*a = *b;
	*b = temp;
}
void swap2(int *a, int *b)//change values using pointers within the functions
{
//Dereferencing is the action of using the pointer in order to reassign the value residing in the original pointed to variable. 
	*a = 17;
	*b = 7;
}
int main()
{
	int a = 10, b = 20;
	printf("Before: A value: %d, B value: %d\n", a, b);
	swap1(&a, &b);
	printf("After: A value: %d, B value: %d\n", a, b);
	printf("Basic swap done\n");

	printf("Before: A value: %d, B value: %d\n", a, b);
	printf("Address of A is : %p, B is: %p\n", &a, &b);
	swap2(&a, &b);
	printf("After: A value: %d, B value: %d\n", a, b);
	printf("New address of A is : %p, B is: %p\n", &a, &b);
}


