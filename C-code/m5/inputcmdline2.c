#include <stdio.h>
//CMD calculator/adder
int main(int argc, char *argv[])
{
	int sum =0;
	for (int count=0; count < argc; count++)
	{
		if (count !=0)
		{
			sum += atoi(argv[count]);
			//sum += strtol(argv[count], NULL)
		}
	}

	printf("sum of %d args is: %d", argc - 1, sum);
	
	
	
	return 0 ;
}
