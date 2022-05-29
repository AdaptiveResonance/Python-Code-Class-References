#include<stdio.h>

int main()
{
	int int_select = 1;
	char chr_select = '6';
	
	switch(int_select)	//int_select is the 'variable' evaulated by the switch to selct proper case response
	{
		case 1:
			printf("case 1 selected\n");
			if(chr_select >'5')
			{
			//Do something 	
			}
			break;
			
		case 2:
			printf("case 2 selected\n");
			break;
		
		default:
			printf("default case\n");
	}
}
