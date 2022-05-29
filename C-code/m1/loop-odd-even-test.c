#include<stdio.h>

int main ()

{
	int index = 0;
	
	for(int index=0; index < 10; index++)  //start at 0 and go up to 10. no ; as that would end the loop of adding
	{
		if(index == 0 ||index == 2 ||index == 4 ||index == 6 ||index == 8 ||index == 10) // checks if even
			printf("*");
	
		else 
			printf("&");		//otherwise is odd
	}
	printf(" %d",index);		//print initial number from top "0"
	
}
