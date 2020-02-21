# Env Check
sudo apt-get update
sudo apt-get install gcc
sudo apt-get install make
sudo apt-get install build-essential
sudo apt-get install ncurses-dev
sudo apt-get install libssl-dev
echo "Environment Check Finished..."

# Deploy
sudo cp -fp syscall_64.tbl ../linux-4.15.2/arch/x86/entry/syscalls/ 
sudo cp -fp syscalls.h ../linux-4.15.2/include/linux/
sudo cp -fp sys.c ../linux-4.15.2/kernel/
echo "Finished"
