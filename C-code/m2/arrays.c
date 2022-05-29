#include<stdio.h>

int main()
{
	int arrint[10];
	int count = 0;// count is declared prior to loop here
	for(; count < sizeof(arrint)/sizeof(int);count++)    //size 10   10x4/4 //count cannot be equal or greater than 10/count
	{
	printf("arrint[%d] = %d\n", count, arrint[count]); //count through the array
	}
	
	//print char strings from arrays
	char arrChar[12]= "Army of Funk";
	char arrChar2[20] = {"this really works!!!"};
	char arrChar3[100]="abc";
	
	printf("arrChar is %s\n", arrChar);
	printf("arrChar2 is %s\n", arrChar2);
	printf("arrChar3 is %s\n", arrChar3);
	printf("arrChar: %p\narrChar2: %p\narrChar3: %p\n", arrChar, arrChar2, arrChar3);
}
