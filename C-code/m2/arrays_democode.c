#include<stdio.h>

int main()
{
	int arrint[10]={1000,2,3,4};
	int count = 0;
	for(; count < sizeof(arrint)/sizeof(int);count++)
	{
	printf("arrint[%d] = %d\n", count, arrint[count]);
	}
	
	char arrChar2[20] = {"this really works!!!"};
	char arrChar[12]= "Army of Funk";
	
	char arrChar3[100]="abc";
	
	printf("arrChar is %s\n", arrChar);
	printf("arrChar: %p\narrChar2 %p\narrChar3 %p\n", arrChar, arrChar2, arrChar3);
}
