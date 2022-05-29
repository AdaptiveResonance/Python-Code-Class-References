#include<stdio.h>

int main()

{
	char arrChar[6] = {'a','b','c','d','e','f','\0'};
	char arrChar2[] = "ABCDEFG";
	
	printf("Printed arrChar is:%s\n", arrChar);
	printf("Printed arrChar2 is:%s\n", arrChar2);

	for(int count = 0; count < 14; count++)
		printf("arrchar[%d]: %c Address: %p\n", count, arrChar[count], &arrChar[count]);



	return(0);

}
