
#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#define MAX_SIZE 1024

int main(void)
{
    int customdev;
    char buf[MAX_SIZE];    //缓冲区
    char get[MAX_SIZE];    //要写入的信息

    char dir[50] = "/dev/customdev";    //设备名

    customdev = open(dir, O_RDWR | O_NONBLOCK);
    if (customdev==-1)
    {
        printf("Cann't open file \n"); exit(0);
        return -1;
    }
    //读初始信息
    read(customdev, buf, sizeof(buf));
    printf("%s\n", buf);

    //写信息
    printf("input :");
    gets(get);
    write(customdev, get, sizeof(get));

      //读刚才写的信息
    read(customdev, buf, sizeof(buf));
    printf("output: %s\n", buf);

    close(customdev);
    return 0;

}

