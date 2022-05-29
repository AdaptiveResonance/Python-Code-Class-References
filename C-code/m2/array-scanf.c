#include<stdio.h>

int main()
{
	int arrint[] = {12,33,44,5,6}; //20bytes of memory array
	long int size = sizeof (arrint)/sizeof(int); //size=5 or 25/5=5
	
	int count;
	for(count = 0; count < size; count++);
	{
	//printf("count after loop: %d\n", count);
	
		printf("Numbers: %d\n", arrint[count]); //will print unassigned garbage?
	}
	//scan input into char arrays to store strings
	char arrchar[20] = {"hell0"};
	char arrchar2[10];
	printf("please enter a string: ");
	scanf(" %[^\n]s",arrchar);
	printf("please enter another string: ");
	scanf("	%[^\n]s",arrchar2);
	printf("first string: %s\n", arrchar);
	printf("first string: %s\n", arrchar2);
	
	scanf("welcome enter a new string %s", arrchar);
	
	return(0);
		
}
