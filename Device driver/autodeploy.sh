echo Start deploying
sudo make
sudo insmod customdev.ko
echo Check dev\:
cat /proc/devices
tail -n 1 /var/log/kern.log
echo -n  "Put in numbers you see ->"
read  main sub
if [[ $main =~ ^-?[0-9]+$ ]] && [[ $sub =~ ^-?[0-9]+$ ]]; then
echo $main $sub
sudo mknod /dev/customdev c $main $sub
echo Check again\:
sudo lsmod
echo Deploy finished\!
#Wrong input handle
else
echo Wrong format!
fi
