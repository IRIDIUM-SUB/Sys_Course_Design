# README

## What to Do

- Add a new char device using module method.

- Read/Write, Open/Close

## Deployment Method

### Environment

Ubuntu 18.04.3 LTS

Kernel: Linux ubuntu 5.0.0-23-generic

### Deploy

1. Unzip the folder to anywhere.

2. Grant `autodeploy.sh` as 777 authority by `sudo chmod 777 autodeploy.sh`

3. Run `autodeploy.sh`.*Note: It's most likely that the major is 240 and the minor is 0. But who knows?*

4. Compile `test.c` by `gcc`: if executable file `test` already exist, skip.

   `gcc -g test.c -o test`

5. Run `sudo ./test`, to see what happens. 

## Some Essential Details

1. Visit `/var/log/kern.log` to get the newest `printk()` message.
2. Use `sudo` to activate