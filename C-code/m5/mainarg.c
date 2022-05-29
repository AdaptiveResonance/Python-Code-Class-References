#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include <sys/types.h>
#include <unistd.h>

// ./mainarg -i 200 -n Unix -c linux -L /home/user/linux/output.txt
// argv[0] -> ./mainarg
// argv[1] ->  -i
// argv[2] ->  200
// argv[3] ->  -n to get n, I then do argv[3][1]
// argc = 9
int main(int argc, char *argv[])
{
    int loops = 0;            // -i
    char change[16] = {'\0'}; // -c
    char name[20] = "";       // -n 
    char path[35] = {'\0'};   // -L
    int argc_idx = 0;         // the arg count
  
   for(argc_idx = 1; argc_idx < argc; argc_idx += 2)
    {
        char select = argv[argc_idx][1];
        //printf("current index: %c\n", select);
        switch(select)
        {
            case 'i':   //  if(argv[argc_idx][1] == 'i' || argv[argc_idx][1] == 'I')
            case 'I':
                printf("Option %c\n",select); 
                int number = atoi(argv[argc_idx+1]);
                printf("value is %d\n", number);
                break;
            case 'c':
            case 'C':
                strcpy(change, argv[argc_idx+1]); // argv[argc_idx+1] is the address of the argc_idx + 1 row
                printf("Option: %c value: %s\n",select, change);
                break;
            case 'n':
            case 'N':
                printf("Option %c\n",select);
                break;
            case 'l':
            case 'L': 
                printf("Option %c\n",select);
                break;
            default:
                printf("Unknown option: %c\n", select);
                break;
        }
    }
    return(45);
}
