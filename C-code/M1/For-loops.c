#include<stdio.h>

int main ()

{
	int index = 0;
	
	for(index = 0 ; index < 5;)
	{
	int aval = ++index;
	
	printf("index: %d\n", aval);
	}
}
	
