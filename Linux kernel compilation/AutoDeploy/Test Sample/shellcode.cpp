#include <stdio.h>
#include <linux/kernel.h>
#include <unistd.h>
#include <string.h>
int main(int argc, char* argv[])
{
	int status=114514;
    if (argc!=4||!strcmp(argv[0],"copy"))
        {
            printf("Usage: copy <src> <dst>\n");
        	return 0;
        }
     else
        {
            printf("Comfirm:%s %s %s\n",argv[1],argv[2],argv[3]);
            status=syscall(333,argv[2],argv[3]);
            if (status==1)
            {
                printf("Failed: Unable to open arc file\n");
            }
            else if (status==2)
            {
                printf("Failed: Unable to open dst file\n");
            }
            else if (status==3)
            {
                printf("Failed: Buffer Overflow\n");
            }
            else if (status==4)
            {
                printf("Failed: Error while cpoying\n");
            }
            else if (!status)
            {
                printf("Success!\n");
            }
            return 0;
        }
printf("%d\n",status);
return 0;
}
