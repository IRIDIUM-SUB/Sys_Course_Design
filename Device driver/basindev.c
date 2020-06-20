
#include <linux/init.h>
#include <linux/module.h>
#include <linux/types.h>
#include <linux/fs.h>    //大部分的驱动程序都会涉及到三个内核数据结构，分别是file_operations、files和inode。它们定义在<lnux/fs.h>中。
#include <linux/sched.h>
#include <linux/cdev.h>
#include <linux/slab.h>
#include <linux/uaccess.h> //copy_to_user

#define DEV_SIZE 2048 //申请空间
MODULE_LICENSE("GPL");
static int dev_major_number = 0;

unsigned char mybuf[DEV_SIZE] = "customdev by POTASSIUM";

static ssize_t my_read(struct file* fp, char __user* userbuf,size_t count,loff_t* pos){
    int size = count;
    if(size>DEV_SIZE){
        printk(KERN_ALERT "out of max");
        size = DEV_SIZE;
    }
    if(copy_to_user(userbuf,mybuf,size)){   //用户空间userbuf向内核空间mybuf拷贝size字节内容
        return -ENOMEM;
    }
    return size;
}

static ssize_t my_write(struct file* fp,const char __user* userbuf,size_t count,loff_t* pos){
    int size = count;
      if(size>DEV_SIZE){
          printk(KERN_ALERT "out of max");
          size = DEV_SIZE;
      }
      if(copy_from_user(mybuf,userbuf,size)){   //内核空间mybuf向用户空间userbuf拷贝size字节内容
          return -ENOMEM;
      }
      return size;
}



static struct file_operations customdev_fops =
{
    //.owner   = THIS_MODULE,
    .read    = my_read,
    .write   = my_write,
};




static int my_init(void)
{
//注册设备
//向系统的字符设备表登记一个字符设备
//major：为0时系统选择一个没有被占用的设备号返回。
//name：设备名
//fops：登记驱动程序实际执行操作的函数的指针
//登记成功，返回设备的主设备号，否则，返回一个负值

	int result = 0;
    printk( KERN_NOTICE "register_device() is called." );//方便调试，KERN_NOTICE日志级别 5
	result = register_chrdev(0, "customdev", &customdev_fops);
    //读取，写入和保存等设备文件操作由存储在file_operations结构中的函数指针处理。
    if(result<0)
        {
            printk("customdev:can\'t register character device with errorcode = %i", result);
            return result;
        }

    dev_major_number = result;
    printk( KERN_NOTICE "customdev: Major = %i \n", dev_major_number);
    return 0;

}

static void my_exit(void)
{
    unregister_chrdev(dev_major_number,"customdev");
    printk("<1>""unregister customdev succeed!\n");
    return;
}

module_init(my_init);
module_exit(my_exit);



