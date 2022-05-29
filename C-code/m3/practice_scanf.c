#include<stdio.h>

int main()
{
	char chArr[] = {'a','b','c','d','e','f'};//char array with no Null terminater
	char chArr2[] = {"ABCDEFG"};	//string array
	printf("first string: %s\n", chArr);
	printf("second stringd: %s\n", chArr2);

	printf("Please enter word: \n");
	scanf("%s", &chArr[0]);			///need " %[^\n]s"   to properly scan both inputs AND a two words input into array 1
	
	printf("Please enter another word: \n");
	scanf("%s", chArr2);
	
	printf("first string entered: %s\n", chArr);
	printf("second string entered: %s\n", chArr2);
	
	return(0);
}

