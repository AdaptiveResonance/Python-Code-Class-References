#include<stdio.h>

int main ()
{
	int array []= {1,2,7,4};

	array[1]=array[2]%5;//7 modulus 5 OR divide 7 by 5 with 2 remainder
	printf("%d", array[1]);   //2
}
