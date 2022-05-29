#include<stdio.h>

int main()
{
	signed int val1 = 5000;
	char ch2;
	
	printf("val1 size of is%lu\n", sizeof(val1)); //size of integer value 4bytes
	printf("ch2 size of is%lu\n", sizeof(ch2));   //size of a character 1byte
	printf("address of val1: %p\n", &val1);		//address of integer value 
	printf("address of ch2: %p\n", &ch2);		//address of character
	
	
	return (0);
	}
//*pointer 8bytes in X64 or 4 in X32
//%d Integer 4bytes
//&f Float 4bytes
//%c Char 1byte
//%lf Double 8bytes
//%ld Long 4bytes (now 8bytes)
//%lld long long 8bytes
//%sd sort (Double precision integer)
//%x hexadecimal output