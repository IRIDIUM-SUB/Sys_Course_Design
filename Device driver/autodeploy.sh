echo "Start deploying";
sudo make;
sudo insmod basindev.ko;
echo "Check dev:";
sudo mknod /dev/customdev c 240 0;
sudo cat /proc/devices| grep "customdev";
echo "Deploy finished!";
