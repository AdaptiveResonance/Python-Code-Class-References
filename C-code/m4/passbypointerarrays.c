#include <stdio.h>
#define SIZE 20		//preprocessor directive
					//prior to the compilation of the program

char *getinput(char *strptr)
{
	int index = 0;
	printf("Enter a string please: ");
	scanf(" %19[^\n]s", strptr);    //strptr = &arr1[size]
	for(index = 0; index < SIZE; index++)
	{
		if(*(strptr + index) == '\0')  //'\0' is equivalent to NULL
		{
		printf("length found is %d\n", index);
		break;
		}
	}
	return(strptr + index);   //address strptr holds = ox7fff..20 conatians lets say 10 and *strptr is 10
}
void reverse(char *strptr, char *end)
{ 
	int length = end - strptr;			//get the length pf the array    ffff30 -ffff20 =10
	for(int index = 0; index < length/2; index++)
	{	
		char temp = *(strptr + index);   //temp == H if array is hello
		*(strptr + index) = *(strptr + length-index-1);
		*(strptr + length-index-1) = temp;
		printf("first %c second: %c \n", *(strptr + index), *(strptr + length-index-1));
	}
	
	/*or while(strptr <= end)
	{
	char temp = *strptr;
	*strptr = *end;
	*end = temp;
	end--;
	strptr++;*/
	}
}
int main()
{	
	const int size = 20;	//This variable is used at runtime and exists throughout the lifetime
	char arr1[20]; //arr[0] == 'h'
	char *last;				//holds addres of last character in the array
	printf("address of arr1 is : %p or %p\n", arr1, &arr1[0]);
	
	last = getinput(&arr1[0]);   //&arr1 == %arr1[0], arr1[size] == the value at location size					//alternatievely arr1
	reverse(arr1, last);	//send beginning and last address of array
	printf("after reverse the array is : %s\n", arr1);

}							





