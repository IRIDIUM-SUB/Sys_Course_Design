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

4. Compile `utilize.c` by `gcc`

5. Run `sudo ./utilize`, to see what happens. 

For more information, see the report. 