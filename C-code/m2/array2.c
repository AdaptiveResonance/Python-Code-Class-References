#include<stdio.h>

int main(void)
{
	char array1[23] = "abc";
	
	array1[4] = 'd';
	printf("%s\n",array1);//print entire string from start but there is no 4th letter [3]
	
	int count;
	for (count = 0; count < 23; count++)
	{
	printf("array1[%d] = %c\n",count,array1[count]); //print each variable counting throug the array
	}


return (0);
}
