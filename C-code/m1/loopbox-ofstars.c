#include<stdio.h>

int main ()

{
	int index = 0;
	
	for(int index=0; index < 45; ++index)  //start at 0 and go up to 45. no ; as that would end the loop of adding
	{
		if(index==8||index==17||index==26||index==35||index==44)	
		printf("*\n");				//create star and new line
		
		else
			if(index == 10 ||index == 12 ||index == 14||index == 16 ||index == 20 ||index == 22||index == 24) //the space numbers to not be printed
			printf(" ");			//create space
	
		else 
			printf("*");		//otherwise is odd, print star
	}
	printf(" %d",index);		//print initial number from top "0"
}
	
