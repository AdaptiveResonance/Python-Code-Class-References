#include <stdio.h>

int main()
{	int value1 = 10, value2 = 20;
	if((value1 > value2) || (value1 < 10))

	printf("%d > %d or %d < 10\n",value1, value2, value1); 

	else
	printf("%d is not less than %d or less than 10\n", value1, value2);// Prints 10 is not less than 20 or less that 10
	
	if( (value1 >= 10) && (value1 < 20))

	printf("%d >= 10 and %d < 20\n", value1, value1);// Prints 10 >= 10 and 10 < 20

	if(value2 != 30)

	printf("%d not equal 30\n", value2); // Prints 20 not equal 30
}
