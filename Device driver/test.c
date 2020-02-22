#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
int main()
{
int testdev;
int i;
char buf[50];
//char prev[50];
testdev =open("/dev/customdev",O_RDONLY | O_WRONLY);
if ( testdev == -1 )
{
printf("%d\n",testdev);
printf("Cann't open file \n");
exit(0);
}

printf("Opened!\n");
printf("Put in string(<50):\n");
fgets(buf,50,stdin);
//printf("%s",buf);
//strcpy(buf, "kksk"); 
write(testdev,buf,50);

read(testdev,buf,50);
printf("Current String:\n");
for (i = 0;buf[i]!='\0';i++)
printf("%c",buf[i]);
printf("\n");
close(testdev);
printf("Device Closed!\n");
}
