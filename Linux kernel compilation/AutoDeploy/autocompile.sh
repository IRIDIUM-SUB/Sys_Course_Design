cd ..
cd linux-4.15.2
echo "Start"
sudo make clean
sudo make -j4 bzImage 
echo "Image Compile Finished"
sudo make -j4 modules 
echo "Modules Finished"
sudo make -j4 modules_install 
echo "Module Installed"
sudo make -j4 install 
echo "Finished"
