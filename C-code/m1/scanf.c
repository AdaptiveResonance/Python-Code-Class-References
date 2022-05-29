#include <stdio.h>

int main()
{
	char character;
	int value1;
	printf("Enter a character: ");
	scanf("%c", &character);
	printf("enter a number: ");
	scanf("%d",&value1);
	printf("the character you entered was: %c\n\n", character);
	printf("the value you entered was: %d\n\n", value1);
	
	return(0);
}
