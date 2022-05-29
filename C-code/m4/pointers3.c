#include<stdio.h>
void input(char *ptr)
{
		printf("enter string, max 30\n");
		scanf(" %29[^\n]s", ptr); //taking input from user, and only 29 characters are accepted. then values stored in memory starting at &arr[0]
}
int printlen(char *ptr)
{
	int counter = 0;
	while(*(ptr+counter) != '\0')   //arr[counter] == *(ptr +counter). &arr[counter] ==ptr+counter
		counter++;
	printf("the length of the string is: %d\n", counter);
}
int main()
{
	char arr[30];
	char *ptr = arr; //same as saying the below
					// declare: char *ptr
					// assigned the value of address of arr[0] to ptr
					//ptr = &arr[0]; &arr[0] = 0x7ffff20; ptr = 0x07ffff20
					//*ptr goes to memory that ptr is pointing to and store a value there
					//This is *ptr = &arr[0]; is invalid
	*ptr = 'a';
	input(arr);//get a string
	printlen(arr);
	
	
}
