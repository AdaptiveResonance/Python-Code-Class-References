#include<stdio.h>	
//reverse/negative loop

int main ()
{
	int index = 0;
	
	for(int index = 0 ; index < 10; --index)  //change -- to ++ to go back to 10
	{
		printf("index: %d\n",index);
		if(index < -20)       //rid this to go back to normal (up to 10)
			break;
		else
			continue;
		printf("hello\n");
	
	}
	printf("at end of loop. index: %d\n", index);
}
